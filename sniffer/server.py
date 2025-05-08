from flask import Flask, request, render_template

# Inicializa o servidor web
app = Flask(__name__, template_folder='web')

@app.route('/')
def index():
    return render_template('index.html')  # Carrega o arquivo index.html da pasta 'web'

# Cria o endpoint /login que aceita requisições POST
@app.route('/login', methods=['POST'])  
def login():
    data = request.json  # Lê o corpo da requisição como JSON
    print("Requisição recebida:", data)  # Exibe os dados recebidos no terminal
    return {"status": "ok"}, 200  # Responde com status de sucesso

if __name__ == '__main__':
    app.run(port=5000)  # Inicia o servidor local na porta 5000
