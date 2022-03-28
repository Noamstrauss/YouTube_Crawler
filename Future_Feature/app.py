from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def form():
    if request.method == "POST":
        username = request.form.get("username")
        search_str = request.form.get("search_str")
        number = request.form.get("number")

        return render_template('form.html' ,username=username,search_str=search_str,number=number)
    return render_template('form.html')




app.run(host='localhost', port=5000, debug=True)