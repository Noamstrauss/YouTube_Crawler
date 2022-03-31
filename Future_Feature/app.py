from flask import Flask, request, render_template
from USER import response

app = Flask(__name__)


@app.route('/', methods=["GET"])
def form():
    return render_template('form.html')


@app.route('/upload', methods=["POST"])
def upload():
    username = request.form.get("username")
    search_str = request.form.get("search_str")
    number = request.form.get("number")
    response(username, search_str, number)

    return render_template('resp.html', username=username, search_str=search_str, number=number)


app.run(host='localhost', port=5858)
