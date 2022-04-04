from flask import Flask, render_template

app = Flask(__name__)

users = ['Капитан Грант', 'Сергей Садовников', 'Джек Воробей',
         'Ридли Скотт', 'Пятнадцатилетний капитан', 'Моби Дик']


@app.route('/distribution')
def distribution():
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')