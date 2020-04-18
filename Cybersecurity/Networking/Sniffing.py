from scapy.all import *

pack = scapy.IP(dst="dgtsec.com", ttl=10)

sniffer = scapy.sniff(iface="Intel(R) Wireless-AC XXXX #2")
sniffer[0].show()

sniffed = sniffer[0]
scapy.hexdump(sniffed.load())

packet = scapy.IP(dst="dgtsec.com")/scapy.ICMP()/"Insecure"
resp = scapy.sr(packet)
