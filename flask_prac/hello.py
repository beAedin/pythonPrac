from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

@app.route('/')
@make_bold
def hello_world():
    return 'Hello, World!!!!'

@app.route('/username/<name>/<int:year>')
def greet(name, year):
    return f"Hello {name} You are {year}"

if __name__ == "__main__":
    app.run(debug=True)