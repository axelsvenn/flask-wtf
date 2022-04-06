from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/table_param/<sex>/<age>')
def table_param(sex, age):
    if sex == "male":
        photo, color = (url_for('static', filename='img/adult.png'), "#0000CD") if int(age) >= 21 else \
            (url_for('static', filename='img/young'), "#4169E1")
    else:
        photo, color = (url_for('static', filename='img/adult.png'), "#FF4500") if int(age) >= 21 else \
            (url_for('static', filename='img/young'), "#FFA07A")

    return render_template('index.html', photo=photo, color=color)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')