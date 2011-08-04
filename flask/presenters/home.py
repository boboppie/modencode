#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Blueprint, render_template, request, redirect, jsonify

# imports
from libs import utils

# models
from models.modmine import Modmine
from models.templates import Templates

home = Blueprint('home', __name__)

@home.route('/')
def index(update=False):
    """
    serve home page
    """
    t = Templates('index') # call Templates.__init__, 'index' is the name of html under templates/home

    if t.exists():
        # fetch data
        m = Modmine()
        catexp_data = m.get_catexp_data(update)

        # TODO: how shall we do "genus" italics?

        time = utils.current_time()

        # **locals(): the variables (time, etc.) that should be available in the context of the template
        html = render_template('home/index.html', **locals())
        t.write(html)

        return t.read()
    else:
        return "index.html template does not exsit..."

@home.route('/update')
def update():
    """
    fetch updates from modmine
    """
    return index(update=True)
