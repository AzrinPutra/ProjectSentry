#!/usr/bin/env python3

import os
import re
import nmap3

#Check for root access to run script
#Exit if not root
##exit("You do not have root priviledges to run this script.\nExiting script.")

#Get target ip from user and store it in targetIp
targetIp = input("Enter the target's IP address: ")
#IP address checker with regular expression for IPv4 address
if not re.match(r'[0-9]+(?:\.[0-9]+){3}', targetIp):
    print("Invalid IP address")
    exit()

print('Your selected target IP is:',targetIp) 

#Enable user to select type of scan(TCP or UDP)

#Enumerate the target IP address with Nmap