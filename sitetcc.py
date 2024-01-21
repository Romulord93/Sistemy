from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de usuários permitidos e senha
allowed_users = ['davi', 'gaab', 'romulo', 'luiz', 'kaua']
password = '12345678'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['usuario']
    entered_password = request.form['senha']

    # Verifica se o usuário está na lista permitida e a senha está correta
    if username in allowed_users and entered_password == password:
        return "Login bem-sucedido!"
    else:
        return "Usuário ou senha incorretos."

if __name__ == '__main__':
    app.run(debug=True)

