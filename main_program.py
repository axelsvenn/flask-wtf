from flask import Flask, render_template, request, url_for

app, i, photos = Flask(__name__), 1, list()


@app.route('/carousel', methods=['POST', 'GET'])
def carousel():
    params = {"title": "Красная планета",
              "css_file": url_for('static', filename='css/style.css'), "photos": photos}

    if request.method == 'POST':
        global i

        with open(f"static/img/photo{i}.png", 'wb') as fd:
            f = request.files["file"]
            fd.write(f.read())
            i, params["photos"] = i + 1, params["photos"] + [url_for("static", filename=f"img/photo{i}.png")]

    return render_template('carousel.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')