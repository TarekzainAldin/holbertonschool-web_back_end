#!/usr/bin/python3
"""Route model for the API"""

from flask import Flask, jsonify, request, abort, redirect, url_for
from sqlalchemy.orm.exc import NoResultFound

from auth import Auth

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    Simple GET route that returns a welcome message.
    """
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
