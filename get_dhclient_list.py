import pprint
from os.path import abspath
from sys import stderr

import pynetbox


def getapi():
    token_file = open('secrets/netbox_token')
    token_slug = token_file.read()
    token_slug = token_slug.strip()
    token_file.close()

    nb = pynetbox.api(
        'http://netbox.robbadler.lan',
        token=token_slug
    )
    return nb

def get_prefixes(nb):
    return nb.ipam.prefixes.all()

def get_static_entries(nb, prefix):
    static_ips = []
    macs = set()
    addresses = nb.ipam.ip_addresses.filter(status='active', assigned_object_type="dcim.interface", parent=prefix)
    for addr in addresses:
        name = ""
        if addr.assigned_object_type == 'dcim.interface':
            ifc = nb.dcim.interfaces.get(id=addr.assigned_object.id)
            name = ifc.device.name
        elif addr.assigned_object_type == 'virtualization.vminterface':
            ifc = nb.virtualization.interfaces.get(id=addr.assigned_object.id)
            name = ifc.virtual_machine.name
        else:
            pprint.pprint(f'{addr} is not a device nor a vm. What is it?', file=stderr)

        if ifc.mac_address is not None:
            static_ips.append({ 'ip-address': addr.address.split('/')[0], 'hostname': name, 'hw-address': ifc.mac_address})
            if ifc.mac_address in macs:
                print(f'{name} [{ifc.mac_address}] MAC already exists! This is a big problem. Fix it.', file=stderr)
                exit(1);
            macs.add(ifc.mac_address)

        else:
            print(f'{name} [{addr}] does not have a MAC address in Netbox. Fix it.', file=stderr)

    return static_ips

