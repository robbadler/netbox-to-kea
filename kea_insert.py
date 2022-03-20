import json

def write_reservations(subnet, reservations):
    with open(f'./kea-dhcp-reservations-{subnet.replace("/", "-")}.json', 'w') as outfile:

        json.dump(reservations, outfile, indent=4)