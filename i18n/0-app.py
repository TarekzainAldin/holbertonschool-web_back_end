#!/usr/bin/python


from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    """render template for index html """
    return render_template('templates/index.html', title='index page')


if __name__ == '__main__':
    app.run(debug=True)
