from flask import Flask, jsonify, abort, make_response, request
from models import library

app = Flask(__name__)
app.config["SECRET_KEY"] = "testowy"

@app.route("/")
def index():
   return render_template("base.html")