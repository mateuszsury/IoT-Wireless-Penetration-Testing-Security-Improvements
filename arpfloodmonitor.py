from scapy.all import sniff, ARP
from plyer import notification
from collections import defaultdict
import time
import threading

# Słownik do przechowywania par IP-MAC
arp_table = defaultdict(str)
# Funkcja do wyświetlania powiadomień systemowych
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Czas trwania powiadomienia w sekundach
    )
# Funkcja do obsługi przechwyconych pakietów ARP
def packet_handler(packet):
    if ARP in packet and packet[ARP].op in (1, 2):  # ARP request (who-has) or ARP reply (is-at)
        src_ip = packet[ARP].psrc
        src_mac = packet[ARP].hwsrc
        if src_ip in arp_table:
            if arp_table[src_ip] != src_mac:
                alert_message = f"ARP Spoofing detected!\nIP: {src_ip}\nOld MAC: {arp_table[src_ip]}\nNew MAC: {src_mac}"
                print(f"ALERT: {alert_message}")  # Powiadomienie w konsoli
                show_notification("ARP Spoofing Alert", alert_message)  # Powiadomienie systemowe
        arp_table[src_ip] = src_mac
# Funkcja do monitorowania ARP
def monitor_arp():
    sniff(filter="arp", prn=packet_handler, store=0)
if __name__ == "__main__":
    print("Starting ARP monitoring...")
    show_notification("ARP Monitor", "Starting ARP monitoring...")
    # Uruchomienie wątku do monitorowania ARP
    monitor_thread = threading.Thread(target=monitor_arp)
    monitor_thread.daemon = True
    monitor_thread.start()
    # Utrzymanie głównego wątku aktywnym
    while True:
        time.sleep(1)
