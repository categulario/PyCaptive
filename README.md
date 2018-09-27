
![alt text](https://raw.githubusercontent.com/ivanlmj/PyCaptive/master/app/static/pycaptive_logo.png)

Authenticated Internet Access for Open Wifi Hotspots.

PyCaptive is an authentication service for Open WiFi Hotspots, working as a Captive Portal, providing Internet Access through its authentication service.

Additionally, PyCaptive also performs the authentication role for Wired networks as well and for network servers that have Transparent Proxy service configured, since that Proxies in Transparent mode, are not capable to provide authentication service.

### Requirements
- Machine: 3.0Ghz; RAM 2Gb; HDD 32Gb; 2 NICs (100/1000Mbps); NIX-Like OS (Debian/Ubuntu)
- Python v3.5
- PIP3 Packages ([Flask, Gunicorn WSGI...](https://github.com/ivanlmj/PyCaptive/blob/master/requirements.txt))
- MongoDB v3.4
- Nginx v1.6
- IPTABLES v1.4
- Routing Configuration for traffic between NICs (IPTABLES)
- Traffic Redirection for Authenticated and Non-Authenticated Users (IPTABLES)

### Installation
- [Here](https://github.com/ivanlmj/PyCaptive/blob/master/deploy/README.md)

For doubts, questions or suggestions: [@ivanleoncz](https://twitter.com/ivanleoncz)
