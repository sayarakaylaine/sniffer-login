from scapy.all import sniff, IP, TCP, UDP  
from datetime import datetime  # Importa a classe datetime para obter o timestamp dos pacotes

# Função que processa cada pacote capturado
def process_packet(packet):
    if IP in packet:  # Verifica se o pacote contém um cabeçalho IP
        # Determina o tipo de protocolo (TCP ou UDP)
        proto = "TCP" if TCP in packet else "UDP" if UDP in packet else "OTHER"

        # Extrai o endereço IP de origem e destino do pacote
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Extrai as portas de origem e destino (para TCP ou UDP)
        # Se for TCP ou UDP, captura as portas correspondentes, caso contrário, marca como "-"
        src_port = packet[TCP].sport if TCP in packet else packet[UDP].sport if UDP in packet else "-"
        dst_port = packet[TCP].dport if TCP in packet else packet[UDP].dport if UDP in packet else "-"

        # Gera um timestamp atual no formato YYYY-MM-DD HH:MM:SS.sss
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        # Extraí o payload (dados) do pacote se for TCP; ignora se for UDP
        payload = bytes(packet[TCP].payload).decode(errors="ignore") if TCP in packet else ""

        # Exibe as informações do pacote capturado no console
        print(f"[{timestamp}] {src_ip}:{src_port} -> {dst_ip}:{dst_port} ({proto})")

        # Se o payload contiver "POST" ou "HTTP", exibe o conteúdo do payload
        if "POST" in payload or "HTTP" in payload:
            print("Payload:\n", payload, "\n")

# Função principal que inicia o sniffer
if __name__ == "__main__":
    print("[*] Iniciando sniffer... Pressione Ctrl+C para parar.")
    # Inicia a captura de pacotes, passando a função de processamento e desabilitando o armazenamento dos pacotes
    sniff(prn=process_packet, store=False)
