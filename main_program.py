from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/table_param/<sex>/<age>')
def table_param(sex, age):
    if sex == "male":
        photo, colour = (url_for('static', filename='img/adult.png'), "background-color: #0000CD;") if int(age) >= 21 else \
            (url_for('static', filename='img/young.jpg'), "background-color: #4169E1;")
    else:
        photo, colour = (url_for('static', filename='img/adult.png'), "background-color: #FF4500;") if int(age) >= 21 else \
            (url_for('static', filename='img/young.jpg'), "background-color: #FFA07A;")

    colour = colour + " width: 450px; height: 400px;"
    return render_template('index.html', photo=photo, colour=colour)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')