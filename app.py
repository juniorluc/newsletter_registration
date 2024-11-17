from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')  # Coleta o email enviado
    if email:
        # Salvar o email em um arquivo ou banco de dados (simples por enquanto)
        with open('subscribers.txt', 'a') as file:
            file.write(f"{email}\n")
        return "Em breve estará recebendo novidades!"
    return "Erro: Por favor, insira um email válido.", 400

if __name__ == '__main__':
    app.run(debug=True)