from app import app
from flask import request, render_template


@app.route('/query-example')
def query_example():
    lang = request.args.get('language')
    frame = request.args.get('framework')
    return f'The lang value is {lang}, the framework is {frame}'


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # обрабатываем POST запрос
    if request.method == 'POST':  # если нам отправили данные
        lang = request.form.get('lang')  # вставляю метки инпута
        frame = request.form.get('frame')
        return render_template('form.html', context=[lang, frame])
    # этот return работает по умолчанию (когда на страницу заходят)
    return render_template('form.html')


@app.route('/json-example')
def json_example():
    return 'JSON'
