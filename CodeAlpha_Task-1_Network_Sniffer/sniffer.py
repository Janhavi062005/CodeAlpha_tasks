from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def handle_packet(packet):
    if IP in packet:
        print("Running")
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        protocol = "OTHER"
        src_port = "-"
        dst_port = "-"

        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        print(
            f"Source IP: {src_ip} | Source Port: {src_port} -> "
            f"Destination IP: {dst_ip} | Destination Port: {dst_port} | "
            f"Protocol: {protocol}"
        )

sniff(count=10, prn=handle_packet)

