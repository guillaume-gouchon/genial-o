from flask import Flask
app = Flask("GENIAL-O")

@app.route("/")
def hello():
    return "Hello World!"
