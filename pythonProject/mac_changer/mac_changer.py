#!/usr/bin/env python3

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")

    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] changing MAC address for " + interface + " to" + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

#def get_current_mac(interface):
    #ifconfig_result = subprocess.check_output(["ifconfig", interface])
    #print(ifconfig_result)

    #mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    #if mac_address_result:
        #print(mac_address_result.group(0))
    #else:
        #print("[-] could not find mac address")
options = get_arguments()
#change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
if mac_address_result:
    print(mac_address_result.group(0))
else:
    print("[-] could not find mac address")