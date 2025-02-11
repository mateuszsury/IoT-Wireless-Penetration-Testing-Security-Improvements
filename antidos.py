import time

def check_rate_limit(host, message_counts, time_window=10, message_limit=5):
    current_time = time.time()  # Pobranie aktualnego czasu
    if host not in message_counts:
        message_counts[host] = []  # Inicjalizacja listy znaczników czasowych dla nowego hosta

    # Filtrowanie listy znaczników czasowych, pozostawiając tylko te, które mieszczą się w określonym przedziale czasowym
    message_counts[host] = [timestamp for timestamp in message_counts[host] if current_time - timestamp < time_window]

    # Sprawdzenie, czy liczba wiadomości przekracza limit
    if len(message_counts[host]) >= message_limit:
        return False  # Limit przekroczony, wiadomość zablokowana
    else:
        message_counts[host].append(current_time)  # Dodanie bieżącego znacznika czasowego
        return True  # Wiadomość dozwolona
