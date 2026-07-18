#!/usr/bin/env python3

import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:22:11:44:11:22", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)