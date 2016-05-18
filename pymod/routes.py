import os

import flask
from flask import request, redirect, send_from_directory, abort

app = flask.Flask('pymod')

@app.route('/')
def root():
    return 'Hello, pymod'
