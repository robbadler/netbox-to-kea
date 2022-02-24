import pprint
from os.path import abspath

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


def get_static_entries(nb):
    static_ips = {}
    addresses = nb.ipam.ip_addresses.filter(status='active', assigned_object_type="dcim.interface")
    for addr in addresses:
        name = ""
        if addr.assigned_object_type == 'dcim.interface':
            ifc = nb.dcim.interfaces.get(id=addr.assigned_object.id)
            name = ifc.device.name
        if addr.assigned_object_type == 'virtualization.vminterface':
            ifc = nb.virtualization.interfaces.get(id=addr.assigned_object.id)
            name = ifc.virtual_machine.name

        if ifc.mac_address is not None:
            static_ips[addr] = {'name': name, 'mac': ifc.mac_address}

    return static_ips

