import ucryptolib
import ubinascii
import hashlib
def simple_pbkdf2(password, iterations, dklen):
    """Uproszczona implementacja PBKDF2 z użyciem SHA-256"""
    password = password.encode('utf-8')  # Konwersja hasła na bajty
    key = hashlib.sha256(password).digest()  # Początkowy skrót hasła
    for _ in range(iterations - 1):
        key = hashlib.sha256(key).digest()
    return key[:dklen]
def derive_key_from_password(password):
    key = simple_pbkdf2(password, 1000, 16)  # Generowanie klucza AES 
    return key
def encrypt_message(message, key):
    cipher = ucryptolib.aes(key, 1)  # AES mode 1 is ECB mode
    padded_message = pad_message(message.encode('utf-8')) 
    encrypted_message = cipher.encrypt(padded_message)  # Szyfrowanie wiadomości
    return ubinascii.b2a_base64(encrypted_message).decode('utf-8').strip()  # Konwersja na base64
def decrypt_message(encrypted_message, key):
    cipher = ucryptolib.aes(key, 1)  # AES mode 1 is ECB mode
    encrypted_message = ubinascii.a2b_base64(encrypted_message)  # 
    decrypted_message = cipher.decrypt(encrypted_message)  # 
    return unpad_message(decrypted_message).decode('utf-8') 
def pad_message(message):
    padding_len = 16 - (len(message) % 16)  # Obliczenie długości wypełnienia
    return message + bytes([padding_len] * padding_len)  # Dodanie wypełnienia
def unpad_message(padded_message):
    # PKCS7 unpadding
    padding_len = padded_message[-1]  # Odczytanie długości wypełnienia
    return padded_message[:-padding_len]  # Usunięcie wypełnienia
