import os

from pymod.mappings import url

import flask
from flask import request, redirect, send_from_directory, abort

app = flask.Flask('pymod')

@app.route('/')
def root():
    return flask.render_template('storefront.html')

@app.route('/<term>')
def search(term):
    where = url('3', term)
    if where:
        return redirect(where)
    else:
        return u"Not found: '{}'".format(term), 404
