#!/usr/bin/env python3

import scapy.all as scapy 

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())
scan("192.168.12.2/24")