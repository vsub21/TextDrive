from flask import Flask
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route("/request")
def request():
	return 0;

@app.route("/response")
def response():
	return 0;

if __name__ == "__main__":
    app.run()