from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {'title': 'Анкета на Марс',
              'surname': 'Садовников',
              'name': 'Сергей',
              'education': 'Наивысшее',
              'profession': 'Инженер-программист',
              'sex': 'male',
              'motivation': 'yandex lyceum',
              'ready': True,
              'css_file': url_for('static', filename='css/style.css')}

    return render_template('index.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
