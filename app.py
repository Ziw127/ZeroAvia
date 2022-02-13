from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("form.html")


if __name__ == '__main__':
    app.debug=True
    # app.run(debug=True, port=8080)
    app.run()
    