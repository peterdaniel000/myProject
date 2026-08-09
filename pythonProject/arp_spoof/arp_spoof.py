#!/usr/bin/env python3

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="192.168.12.135", hwdst="00:0c:29:9c:1b:92", psrc="192.168.12.1")
