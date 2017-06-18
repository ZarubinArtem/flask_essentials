from flask import Flask
from flask import render_template
# from flask import request

app = Flask(__name__)

# add a route
@app.route('/')
@app.route('/<name>')
def index(name="Josh"):
    # name = request.args.get('name', name)
    context = {"name":name}
    return render_template("index.html", **context)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    context = {'num1':num1, 'num2':num2, 'answer':num1+num2}
    return render_template("add.html", **context)


# run the app
app.run(debug=True)
