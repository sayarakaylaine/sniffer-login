
# Projeto: Sniffer + Página de Login

## 📌 Visão Geral

Este projeto simula tráfego HTTP gerado por uma página de login, capturado por um sniffer desenvolvido em Python com Scapy. O objetivo é demonstrar como dados trafegam pela rede e como podem ser visualizados por ferramentas de análise.

- A página `index.html` permite o envio de usuário e senha via POST para um backend Flask.
- O sniffer intercepta e exibe no terminal informações como timestamp, IPs, portas e payload dos pacotes HTTP/TCP ou UDP.

---

## ⚙️ Pré-requisitos e Instalação

### Ambiente

- **Sistema:** Linux ou WSL (Windows Subsystem for Linux)
- **Python 3.8+**
- **VS Code** (ou qualquer editor)

### Instalação das dependências

```bash
pip install scapy flask
```

> ⚠️ O sniffer utiliza **raw sockets**, por isso **precisa ser executado como root**.

---

## ▶️ Como Executar o Projeto

### 1. Iniciar o Sniffer

```bash
cd sniffer
sudo python3 sniffer.py
```

O sniffer irá capturar e exibir pacotes com:

- Timestamp
- IP de origem e destino
- Portas
- Payload contendo "POST" ou "HTTP"

### 2. Iniciar o Servidor Flask da Página de Login

Em outro terminal:

```bash
cd sniffer  # A pasta web está dentro desta pasta
python3 server.py
```

O servidor estará disponível em: [http://localhost:5000](http://localhost:5000)

### 3. Acessar a Página de Login

- Acesse manualmente [http://localhost:5000](http://localhost:5000)
- Preencha os campos de **usuário** e **senha**
- Clique em "Enviar" para gerar a requisição POST

> Você verá no terminal do Flask algo como:
> `Requisição recebida: {'username': 'admin', 'password': '123456'}`

---

## 🚀 Contribuição

Projeto acadêmico desenvolvido para demonstrar princípios de captura de pacotes e segurança de dados em redes.

---

## 🧠 Observação Final

Este projeto é **educacional** e visa reforçar a compreensão sobre:

- Como funciona o tráfego de dados HTTP.
- Como sniffer pode capturar dados sensíveis.
- A importância de segurança no transporte de informações (ex: uso de HTTPS).
