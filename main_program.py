from flask import Flask, render_template, request, url_for

app, i = Flask(__name__), 1


@app.route('/carousel', methods=['POST', 'GET'])
def carousel():
    params = {"title": "Красная планета",
              "css_file": url_for('static', filename='css/style.css'), "photos": []}

    if request.method == 'GET':
        return render_template('carousel.html', **params)

    elif request.method == 'POST':
        global i

        with open(f"static/img/photo{i}.png", 'wb') as fd:
            f = request.files["file"]
            fd.write(f.read())
            i, params["photos"] = i + 1, params["photos"] + [url_for("static", filename=f"img/photo{i}.png")]

        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')