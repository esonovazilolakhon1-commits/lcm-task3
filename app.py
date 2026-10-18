from math import lcm
from flask import Flask, request

app = Flask(__name__)


@app.route("/esonovazilolakhon1_gmail_com")
def calc():
    x = request.args.get("x", "")
    y = request.args.get("y", "")
    if not (x.isascii() and x.isdigit() and y.isascii() and y.isdigit()):
        return "NaN", 200, {"Content-Type": "text/plain"}
    return str(lcm(int(x), int(y))), 200, {"Content-Type": "text/plain"}
