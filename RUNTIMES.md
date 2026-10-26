# Runtime and validation matrix

The Python files are research experiments accompanying the Polish dissertation.
They do not form a single application or a production service.

* Desktop CPython: ARP and HTTP monitoring/experiments use Scapy, Plyer and/or
  Requests. Install `requirements-cpython.txt` in an isolated virtual environment.
* MicroPython: files importing `network`, `espnow`, `ujson` or `machine` require
  supported ESP32 firmware and a deliberately configured lab setup. Desktop pip
  does not supply those firmware modules.

CI checks syntax only; it does not transmit packets, prove defensive efficacy,
or claim hardware compatibility. Hardware experiments require explicit lab
scope, isolated devices and recorded firmware/channel/configuration parameters.
