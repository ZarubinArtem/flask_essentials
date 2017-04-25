from flask import Flask
# from flask import request

app = Flask(__name__)

# add a route
@app.route('/')
@app.route('/<name>')
def index(name="Josh"):
    # name = request.args.get('name', name)
    return "It's work, {0}".format(name)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    # return "{} + {} = {}".format(num1, num2, num1+num2)
    return """
<!doctype html>
<html>

    <head><title> Adding stuff </title></head>

    <body>
        <h1> {} + {} = {} </h1>
    </body>

</html>
""".format(num1, num2, num1+num2)


# run the app
app.run(debug=True)
