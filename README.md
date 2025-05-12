# Projeto Sniffer + Página de Login

## 📌 Visão Geral

Este projeto simula a captura de tráfego HTTP entre uma página de login e um servidor Flask local. Um sniffer desenvolvido em Python com `socket` e `scapy` intercepta pacotes de rede e exibe no console informações como:

- Timestamp
- IP de origem e destino
- Portas de origem e destino
- Payload (conteúdo dos pacotes)

A interface HTML simples envia requisições POST via `fetch()` para o backend local, gerando tráfego capturado pelo sniffer.
---

## ⚙️ Pré-requisitos e Instalação

- Python 3
- Scapy
- Flask
  
### Sistema operacional recomendado:
- **Linux** (ou **WSL** no Windows)

### Instale as dependências:
```bash
pip install scapy flask
```

## 🚀 Como Executar o Sniffer

### 1. Acesse o diretório do sniffer:

```bash
cd sniffer
```

### 2. Execute com permissões elevadas:

```bash
sudo python3 sniffer.py
```

### 3. O sniffer iniciará e mostrará os pacotes capturados diretamente no terminal.

## 🌐 Como Iniciar a Página de Login

### 1. Ainda no diretório do projeto, inicie o servidor Flask:

```bash
python3 sniffer/server.py
```

### 2. Acesse a página de login no navegador:

`http://127.0.0.1:5000`

### 3. Preencha o formulário e envie. O backend receberá os dados e os pacotes serão capturados pelo sniffer.


