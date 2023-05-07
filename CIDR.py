#!/usr/bin/env python3

# Usage: <ip>/<cidr> (e.g 192.168.0.0/24)

import sys

# Converd CIDR to subnet mask
def cidr_to_mask(ID):
    subnet = []
    for i in range(32):
        if (i < ID):
           subnet.append(1)
        else:
           subnet.append(0)
    results = []
    for j in range(0,32,8):
        # https://www.geeksforgeeks.org/python-binary-list-to-integer/
        result = int("".join(str(x) for x in subnet[j:j+8]), 2)
        results.append(result)
    mask = ".".join(str(x) for x in results)
    return mask

# Count hosts available in a given IP range
def host_count(ID):
    count = 2**(32-int(ID)) - 2
    return count

# Compute gateway IP address
def gateway(IP, ID):
    (num1, num2, num3, num4) = IP.split('.')
    ip = [int(num1), int(num2), int(num3), int(num4)]
    hosts = host_count(ID)+2
    # IP address construction
    if (hosts <= 256):
        ip[3] = hosts-1
    elif (hosts > 256 and hosts <= 256*256):
        tmp = hosts
        pos3 = int(tmp/256-1)
        pos4 = int(hosts-(256*pos3)-1)
        ip[2] = pos3
        ip[3] = pos4
    elif (hosts > 256*256 and hosts <= 256*256*256):
        tmp1 = hosts
        tmp2 = hosts
        pos2 = int(tmp1/(256*256)-1)
        pos3 = int((tmp2-pos2*256*256)/256-1)
        pos4 = int((hosts-pos2*256*256-pos3*256)-1)
        ip[1] = pos2
        ip[2] = pos3
        ip[3] = pos4
    elif (hosts > 256*256*256 and hosts <= 256*256*256*256):
        tmp1 = hosts
        tmp2 = hosts
        tmp3 = hosts
        pos1 = int(tmp1/(256*256*256)-1)
        pos2 = int((tmp2-pos1*256*256*256)/(256*256)-1)
        pos3 = int((tmp3-pos1*256*256*256-pos2*256*256)/256-1)
        pos4 = int((hosts-pos1*256*256*256-pos2*256*256-pos3*256)-1)
        ip[0] = pos1
        ip[1] = pos2
        ip[2] = pos3
        ip[3] = pos4
    address = ".".join(str(x) for x in ip)
    return address

# Main program
if __name__=="__main__":
    if len(sys.argv) == 2:
        (addr, cidr) = sys.argv[1].split('/')
        print(f"IP address: {addr}\n\
CIDR: {cidr}\n\
Subnet mask: {cidr_to_mask(int(cidr))}\n\
Host count: {host_count(cidr)}\n\
Network ID: {addr}\n\
Gateway: {gateway(addr, cidr)}\n\
Address range: {addr} - {gateway(addr,cidr)}")
