from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get("http://express-service:3000")
    return render_template("index.html", message=response.json())

app.run(host="0.0.0.0", port=5000)
