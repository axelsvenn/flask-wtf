from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    param = {"title": "Заготовка"
             }
    return render_template('index.html', **param)


@app.route("/training/<prof>")
def training(prof):
    param = {"title": "Тренировки в полёте",
             "prof": prof
             }
    return render_template('training.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
