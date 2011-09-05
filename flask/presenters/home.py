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
        modmine_path = config.DATASOURCE_ROOT + "/" # make it work for modminetest for now, will switch to the next line
        # modmine_path = config.DATASOURCE_ROOT + "/" + m.get_webapp_path(update)
        # or modmine_path = config.DATASOURCE_ROOT + "/query/"
        gbrowse_base = m.get_gbrowse_base()

        time = utils.current_time()

        from models.publications import publications

        # **locals(): the variables (time, etc.) that should be available in the context of the template
        html = render_template('home/index.html', **locals())
        t.write(html) # create a new static/html/index.html if not exist

    return t.read()

@home.route('/update')
def update():
    """
    fetch updates from modmine
    """
    return index(update=True)

@home.route('/publications')
def publications():
    """
    serve publications page
    """
    t = Templates('publications')

    if not t.exists():
        # TODO fetch data
        html = render_template('home/publications.html', **locals())
        t.write(html)

    return t.read()
    
@home.route('/about')
def about():
    """
    serve about page
    """
    return render_template('home/about.html')

@home.route('/fly_2010pubs')
def fly_2010pubs():
    """
    serve fly pubs page
    """
    return render_template('home/fly_2010pubs.html')

@home.route('/worm_2010pubs')
def worm_2010pubs():
    """
    serve worm pubs page
    """
    return render_template('home/worm_2010pubs.html')

@home.route('/howtopubs')
def howtopubs():
    """
    serve data format page
    """
    return render_template('home/howtopubs.html')

@home.route('/dcc')
def dcc():
    """
    serve dcc page
    """
    return render_template('home/dcc.html')

