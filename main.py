#!/usr/bin/env python3
# vim: set fileencoding=UTF-8 :

import pprint

from get_dhclient_list import getapi, get_static_entries, get_prefixes
import kea_insert

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    pprint.pprint(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    nb = getapi()
    pprint.pprint(nb.status())

    prefixes = []
    for pre in get_prefixes(nb):
        prefixes.append(pre.prefix)

    for pre in prefixes:
        if "192.168.1" in pre:
            continue

        static_ips = get_static_entries(nb, pre)
        pprint.pprint(pre)
        pprint.pprint(static_ips)

        if len(static_ips):
            kea_insert.write_reservations(pre, static_ips)
