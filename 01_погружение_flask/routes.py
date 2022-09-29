from app import app
# из файла app.py импортирую переменную app
from flask import request, render_template


@app.route('/')  # создал первый путь (главную страницу) на сайте
def index():
    user_agent = request.headers.get('User-Agent')
    content = f'<h1>Hello!</h1><p>Your browser is {user_agent}</p>'
    return render_template('index.html', title='Главная')


@app.route('/user/<username>')
def user(username):
    # f-строка позволяет вставить внутрь строки значение переменной в {}
    content = f'<h1>Hello, {username}!</h1>'
    return content
