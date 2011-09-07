#!/usr/bin/python
# -*- coding: utf -*-

import config

# framework
from flask import Blueprint, render_template, request, redirect, url_for

# imports
from libs import utils
from functools import wraps

# models
from models.modmine import Modmine
from models.templates import Templates
from models.constants import *

home = Blueprint('home', __name__)

def match_ip(f):
    """
    match a specific ip address when calling this function
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        remote = request.remote_addr
        for ip in config.ALLOWED_IP:
            if remote.startswith(ip):
                return f(*args, **kwargs)
        return redirect(url_for('app.code_401', ip=remote))
    return decorated_function

@home.route('/')
def index(update=False):
    """
    serve home page
    """
    t = Templates('index')

    if update or not t.exists():
        m = Modmine()
        data = m.get_catexp_data()
        gbrowse_base = m.get_gbrowse_base()
	
        time = utils.current_time()

        from models.publications import publications as modencode_publications

        html = render_template('home/index.html', **dict(locals().items() + globals().items()))
        t.write(html)

    return t.read()

@home.route('/update')
@match_ip
def update():
    """
    fetch updates from modmine
    """
    return index(update=True)