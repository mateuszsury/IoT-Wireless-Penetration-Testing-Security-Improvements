# IoT Wireless Penetration Testing&Security Improvements

This repository contains a comprehensive suite of penetration testing tools, scripts, and detailed documentation focused on the security of various wireless communication protocols in the context of IoT devices. It is intended for security professionals, network administrators, and researchers interested in identifying vulnerabilities and implementing effective countermeasures in wireless home automation systems.

---

## Table of Contents

- [Introduction](#introduction)
- [Comprehensive Documentation](#comprehensive-documentation)
- [Scripts and Tools](#scripts-and-tools)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Introduction

Wireless networks powering IoT and home automation systems are increasingly exposed to a wide range of security threats. This repository aims to provide a practical and theoretical framework for understanding and testing these vulnerabilities. The collection of scripts simulates various attacks—ranging from Denial-of-Service (DoS) and Distributed DoS (DDoS) to ARP poisoning and man-in-the-middle (MitM) techniques—while the documentation outlines both the attack methodologies and the corresponding security measures required to mitigate them.

---

## Comprehensive Documentation

The core of this repository is the detailed documentation contained in the file **"Analiza bezpieczeństwa i niezawodności bezprzewodowych systemów automatyki domowej.pdf"**. This document (written in Polish) provides an in-depth analysis of the penetration tests used in the work, including but not limited to attacks such as DoS/DDoS (e.g., HTTP Flood, TCP SYN Flood, Jamming, ARP Poisoning), WiFi password attacks (e.g., Evil Twin, Dictionary, Brute Force, Packet Sniffing), MitM attacks, attacks targeting devices operating in ad hoc mode (including specialized attacks on ESPNow networks), as well as attacks on Bluetooth and ZigBee devices.

Additionally, it thoroughly describes a range of security measures—covering protection against deauthentication, jamming, ARP poisoning, password attacks, DoS/DDoS assaults, and more—offering guidelines on the use of technologies like WPA3, dynamic frequency hopping, rate limiting, and encryption protocols (WPA3/TLS/HTTPS). This comprehensive resource is essential for understanding both the offensive techniques and the defensive strategies applicable to modern wireless home automation systems.

---

## Scripts and Tools

The repository includes several Python scripts that simulate attacks and monitor network security:

### Attack Simulation

- **`requestdos.py`**\
  Simulates an HTTP flood attack by sending a barrage of requests to a target URL.\
  *Usage:* Call `send_request(target_url)` with the desired target.

- **`arpattack.py`**\
  Executes an ARP spoofing attack aimed at isolating a target device by poisoning its ARP cache.\
  *Usage:* Run `arp_spoof(target_ip, gateway_ip)`\
  *Dependencies:* `scapy` (including ARP, send, get\_if\_hwaddr, conf, srp, Ether), `time`

- **`mitmespnow.py`**\
  Demonstrates a man-in-the-middle (MitM) attack on devices communicating via ESPNow by intercepting, altering, and re-transmitting sensor data, thereby disrupting genuine communications.

- **`dosespnow.py`**\
  Conducts a DoS attack on ESPNow-based devices by flooding them with excessive messages, effectively overloading the recipient.

### Network Monitoring & Defense

- **`floodalert.py`**\
  Monitors network traffic to detect HTTP flood attacks and raises an alert when such activity is detected.\
  *Dependencies:* `plyer`, `scapy`, `collections`, `time`\
  *Usage:* Invoke `monitor_http_requests()` to start monitoring.

- **`arpfloodmonitor.py`**\
  Continuously monitors the ARP table for suspicious changes, providing alerts when an attack is detected.\
  *Dependencies:* `scapy`, `plyer`, `collections`, `time`, `threading`\
  *Usage:* Use `monitor_arp()` to initiate ARP monitoring.

- **`espnowtorf.py`**\
  Detects RF signal jamming in ESPNow networks, serving as an early warning system for potential DoS scenarios.

- **`espnowantidos.py`**\
  Implements a rate limiter to mitigate DoS risks in ESPNow communications by preventing any single device—or the network overall—from receiving an unsustainable number of messages.

### Security & Encryption

- **`encryption.py`**\
  A MicroPython library that adds encryption capabilities to ESPNow messages, securing communications against interception and modification.

---

## Dependencies

The provided scripts rely on several Python libraries and modules, including:

- **Scapy:** For packet crafting, sniffing, and network manipulation.
- **Plyer:** For displaying system notifications.
- **Collections:** For managing data structures (e.g., dictionaries) in monitoring scripts.
- **Time:** For managing delays and timeouts.
- **Threading:** For concurrent execution in monitoring scripts.

Ensure that all dependencies are installed in your testing environment. Some tools may require running in a controlled or virtualized setup to avoid disrupting production networks.

---

## Usage

Each script is designed to be executed either as a standalone tool or integrated into a larger testing framework. Detailed instructions and usage examples are provided as inline comments within each script. It is imperative that these tools be used exclusively in authorized and controlled environments for educational and research purposes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for full license details.
