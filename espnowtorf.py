import network
import espnow
import machine
import time
import _thread
from rfm69 import RFM69

# Ustawienia dla modułu RF 433 MHz
rf_cs_pin = machine.Pin(5, machine.Pin.OUT)
rf_reset_pin = machine.Pin(17, machine.Pin.OUT)
rf_interrupt_pin = machine.Pin(16, machine.Pin.IN)
rf_protocol_active = False
# Inicjalizacja RFM69
rfm = RFM69(spi=machine.SPI(1), cs=rf_cs_pin, reset=rf_reset_pin, interrupt=rf_interrupt_pin, frequency=433)
rfm.set_params(
    modulation="FSK",
    bitrate=2000,
    frequency_deviation=5000,
    rx_bandwidth=50000,
    rssi_threshold=-114,
    sync_word=[0x2D, 0xD4],
    power_level=13,
    encryption_key=b"sampleEncryptKey"
)
# Inicjalizacja ESP-NOW
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
espnow.init()
# Adres MAC odbiornika ESP-NOW
peer = b'\xFF\xFF\xFF\xFF\xFF\xFF'
espnow.add_peer(peer)
# Flaga zakłóceń
interference_detected = False
# Czas ostatniej otrzymanej wiadomości
last_received_time = time.time()
# Funkcja do monitorowania poziomu sygnału RSSI
def get_rssi():
    wlan.scan()  # Potrzebne do aktualizacji informacji RSSI
    time.sleep(1) 
    return wlan.status('rssi')
def send_espnow():
    global rf_protocol_active
    while True:
        if not rf_protocol_active:
            message = "Hello from ESP-NOW"
            espnow.send(peer, message)
            print("ESP-NOW message sent")
            time.sleep(1)
        else:
            time.sleep(1)
def recv_espnow():
    global last_received_time
    while True:
        host, msg = espnow.recv()
        if msg:
            last_received_time = time.time()
            print("ESP-NOW message received: ", msg)
def check_interference():
    global interference_detected, rf_protocol_active, last_received_time
    rssi_threshold = -80  # Próg RSSI wskazujący na możliwe zakłócenia
    while True:
        current_time = time.time()
        rssi = get_rssi()
        print("Current RSSI:", rssi)

        if current_time - last_received_time > 3 or rssi < rssi_threshold:
            interference_detected = True
        else:
            interference_detected = False

        if interference_detected:
            print("Interference detected, switching to RF 433 MHz")
            rf_protocol_active = True
        else:
            print("No interference, using ESP-NOW")
            rf_protocol_active = False

        time.sleep(1)
def send_rf():
    while True:
        if rf_protocol_active:
            # Kod nadawania wiadomości przez RF 433 MHz
            message = "Hello from RF 433 MHz"
            rfm.send(message.encode('utf-8'))
            print("RF 433 MHz message sent")
            time.sleep(1)
        else:
            time.sleep(1)  # Przerwa, gdy RF 433 MHz jest nieaktywne
# Uruchomienie wątków
_thread.start_new_thread(send_espnow, ())
_thread.start_new_thread(recv_espnow, ())
_thread.start_new_thread(check_interference, ())
_thread.start_new_thread(send_rf, ())
while True:
    time.sleep(1)
