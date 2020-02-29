from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! <h2>Hello world!</h2>"

if __name__ == '__main__':
    app.run()