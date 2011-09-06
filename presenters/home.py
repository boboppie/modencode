#!/usr/bin/python
# -*- coding: utf -*-

import config

# framework
from flask import Blueprint, render_template, request, redirect, jsonify

# imports
from libs import utils

# models
from models.modmine import Modmine
from models.templates import Templates
from models.constants import *

home = Blueprint('home', __name__)


@home.route('/')
def index(update=False):
    """
    serve home page
    """
    t = Templates('index') # create a new Template object from "static/html/index.html", it doesn't exist the first call

    if update or not t.exists():
        # fetch data
        m = Modmine()
        data = m.get_catexp_data()
        gbrowse_base = m.get_gbrowse_base()
	
        time = utils.current_time()

        from models.publications import publications as modencode_publications

        html = render_template('home/index.html', **dict(locals().items() + globals().items()))
        t.write(html) # create a new static/html/index.html if not exist

    return t.read()

@home.route('/update')
def update():
    """
    fetch updates from modmine
    """
    return index(update=True)