from flask import Flask, render_template
from django.core.management import utils

app = Flask(__name__)

@app.route("/")
def home():
    key:str = utils.get_random_secret_key()
    return render_template("index.html", key=key)

if __name__ == "__main__":
    app.run(debug=True)