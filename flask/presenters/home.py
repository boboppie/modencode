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
from models.constant import *

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
	
        intermine_url = INTERMINE_URL
	modmine_rel = MODMINE_REL
        gbrowse_url = GBROWSE_URL
        dataset_search_url = DATASET_SEARCH_URL

	#aFly = ORG_MAP['D. pseudoobscura']
	
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
    intermine_url = INTERMINE_URL
    gbrowse_url = GBROWSE_URL
    dataset_search_url = DATASET_SEARCH_URL

    return render_template('home/about.html',**locals())

@home.route('/fly_2010pubs')
def fly_2010pubs():
    """
    serve fly pubs page
    """
    intermine_url = INTERMINE_URL
    gbrowse_url = GBROWSE_URL
    dataset_search_url = DATASET_SEARCH_URL
    return render_template('home/fly_2010pubs.html',**locals())

@home.route('/worm_2010pubs')
def worm_2010pubs():
    """
    serve worm pubs page
    """
    intermine_url = INTERMINE_URL
    gbrowse_url = GBROWSE_URL
    dataset_search_url = DATASET_SEARCH_URL
    return render_template('home/worm_2010pubs.html',**locals())

@home.route('/howtopubs')
def howtopubs():
    """
    serve data format page
    """
    intermine_url = INTERMINE_URL
    gbrowse_url = GBROWSE_URL
    dataset_search_url = DATASET_SEARCH_URL
    return render_template('home/howtopubs.html',**locals())

@home.route('/dcc')
def dcc():
    """
    serve dcc page
    """
    intermine_url = INTERMINE_URL
    gbrowse_url = GBROWSE_URL
    dataset_search_url = DATASET_SEARCH_URL
    return render_template('home/dcc.html',**locals())

