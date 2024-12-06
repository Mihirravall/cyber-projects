from scapy.all import sniff

def packet_callback(packet):
    print(packet.show())

# Capture packets (you can specify interface and filter)
sniff(prn=packet_callback, store=0)
