# netbox-to-kea

Create a ./secrets directory. Add file `netbox-token` holding a read-only token string.

Invoke `python3 main.py` to scrape all defined prefixes (subnets) in Netbox, and writing out reservation files in Kea format.

I added these reservations files in Kea as `/etc/kea/reservations.d`, and made reference to them in `/etc/kea/kea-dhcp4.conf` as the value of a `reservations` key:
```
Dhcp4:
  subnet4:
    [0]:
      "reservations": <?include "/etc/kea/reservations.d/kea-dhcp-reservations-192.168.20.0-24.json"?>
