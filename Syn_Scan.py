from scapy.all import *
from scapy.layers.inet import TCP
import ipaddress

ports = [25, 53, 80, 443, 445, 8080, 8443]

def SynScan(host):
    SYN = 0x02
    ACK = 0x10
    SYN_ACK = SYN | ACK  # 0x12

    ans,unans = sr(
        IP(dst=host)/
        TCP(sport=33333,dport=ports,flags="S")
        ,timeout=2,verbose=0)
    print("Open ports at %s:" % host)
    for (s,r,) in ans:
        # Check for SYN+ACK response using named constants for clarity
        if s[TCP].dport == r[TCP].sport and r[TCP].flags & SYN_ACK == SYN_ACK:
            print(s[TCP].dport)
def DNSScan(host):
    for snd, rcv in ans:
        if rcv.haslayer(UDP):
            print("DNS Server at %s"%host),timeout=2,verbose=0)
    for snd, rcv in ans:
        if rcv.haslayer(UDP):
            print("DNS Server at %s"%host)
        print("DNS Server at %s"%host)

host = input("Enter target IP address: ")
    
try:
    ipaddress.ip_address(host)
except ValueError:
    print("Invalid address")
    exit(-1)

import threading

# Run scans concurrently
t1 = threading.Thread(target=SynScan, args=(host,))
t2 = threading.Thread(target=DNSScan, args=(host,))

t1.start()
t2.start()

t1.join()
t2.join()
