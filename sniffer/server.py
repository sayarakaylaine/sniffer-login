from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='web')

@app.route('/')
def index():
    return render_template('index.html')

# Rota para servir app.js diretamente da pasta 'web'
@app.route('/sniffer/web/app.js')
def serve_app_js():
    return send_from_directory(os.path.join(app.root_path, 'web'), 'app.js')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    print("Requisição recebida:", data)
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(port=5000)
