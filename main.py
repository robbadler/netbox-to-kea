# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pprint

from get_dhclient_list import getapi, get_static_entries


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    nb = getapi()
    pprint.pprint(nb.status())

    static_ips = get_static_entries(nb)
    pprint.pprint(static_ips)
