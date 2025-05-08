# Importa Flask para criar o servidor e request para ler os dados recebidos
from flask import Flask, request  

# Inicializa o servidor web
app = Flask(__name__)  

# Cria o endpoint /login que aceita requisições POST
@app.route('/login', methods=['POST'])  
def login():
    data = request.json  # Lê o corpo da requisição como JSON
    print("Requisição recebida:", data)  # Exibe os dados recebidos no terminal
    return {"status": "ok"}, 200  # Responde com status de sucesso

if __name__ == '__main__':
    app.run(port=5000)  # Inicia o servidor local na porta 5000
