from flask import Flask, request, render_template
from response import response

app = Flask(__name__, static_folder='static')


@app.route('/', methods=["GET"])
def form():
    return render_template('form.html')


@app.route('/upload', methods=["POST"])
def upload():
    username = request.form.get("username")
    search_str = request.form.get("search_str")
    response(username, search_str)

    return render_template('resp.html', username=username, search_str=search_str)


app.run(host='localhost', port=8081)
