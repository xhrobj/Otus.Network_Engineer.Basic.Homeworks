from scapy.all import ARP, send

"""Тест отправки arp-запроса, используя библиотеку scapy"""

arp_request = ARP(pdst="192.168.1.55")
send(arp_request)

print("Hello, Scapy")