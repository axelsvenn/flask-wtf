from flask import Flask, render_template

app = Flask(__name__)


@app.route('/carousel')
def carousel():
    # file_carousel = lambda x: url_for('static', filename=f'img/{x}')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')