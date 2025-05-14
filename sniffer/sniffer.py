from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

def process_packet(packet):
    if IP in packet:
        proto = "TCP" if TCP in packet else "UDP" if UDP in packet else "OTHER"
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport if TCP in packet else packet[UDP].sport if UDP in packet else "-"
        dst_port = packet[TCP].dport if TCP in packet else packet[UDP].dport if UDP in packet else "-"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        print(f"[{timestamp}] {proto} {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

        # Captura e exibe o payload se houver camada Raw
        if packet.haslayer(Raw):
            payload = packet[Raw].load.decode(errors="ignore")
            if "POST" in payload or "HTTP" in payload or "username" in payload or "password" in payload:
                print("Payload:")
                print(payload)
                print("-" * 60)

if __name__ == "__main__":
    print("[*] Iniciando sniffer... Pressione Ctrl+C para parar.")
    try:
        sniff(prn=process_packet, store=False)
    except KeyboardInterrupt:
        print("\n[*] Sniffer finalizado pelo usuário.")
