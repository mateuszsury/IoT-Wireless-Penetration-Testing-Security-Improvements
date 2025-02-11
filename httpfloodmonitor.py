from plyer import notification
from scapy.all import sniff
from collections import defaultdict
import time

# Słownik do przechowywania liczby zapytań HTTP
http_requests = defaultdict(int)
# Funkcja do wyświetlania powiadomień systemowych
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Czas trwania powiadomienia w sekundach
    )
# Funkcja do obsługi przechwyconych pakietów
def packet_handler(packet):
    global http_requests
    if packet.haslayer('TCP') and packet.dport == 80:
        ip_src = packet['IP'].src
        http_requests[ip_src] += 1
# Funkcja do monitorowania liczby zapytań i wykrywania ataków
def monitor_http_requests():
    global http_requests
    while True:
        time.sleep(1)
        for ip, count in list(http_requests.items()):
            if count > 100:  # Próg dla wykrycia ataku
                message = f"Detected HTTP Request Flood from {ip} with {count} requests in the last second."
                print(f"ALERT: {message}")  # Powiadomienie w konsoli
                show_notification("HTTP Request Flood Alert", message)  # 
                del http_requests[ip]
            else:
                http_requests[ip] = 0
if __name__ == "__main__":
    import threading
    monitor_thread = threading.Thread(target=monitor_http_requests)
    monitor_thread.daemon = True
    monitor_thread.start()
    # Przechwytywanie ruchu sieciowego
    sniff(prn=packet_handler, store=0)
