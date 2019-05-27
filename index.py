# -*- coding:utf8 -*-

from flask import Flask, render_template, request, jsonify
from service import Service

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/category", methods=["POST"])
def category():
    fr = request.form
    p_id = request.form["p_id"]
    type_ = request.form["type"]
    rows = Service.select_category(type_, p_id)
    return jsonify(rows)


@app.route("/get_price", methods=["POST"])
def get_price():
    c_id = request.form["c_id"]
    length = request.form["length"]
    rows = Service.select_price(c_id, length)
    return jsonify(rows)


if __name__ == "__main__":
    app.run()
