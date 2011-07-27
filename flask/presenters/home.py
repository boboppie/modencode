#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Blueprint, render_template, request, redirect

# models
from models.modmine import Modmine
from models.templates import Templates

home = Blueprint('home', __name__)

@home.route('/')
def index(update=False):
    """
    serve home page
    """
    t = Templates()

    # TODO: force update on missing static html

    if update:
        # fetch data
        m = Modmine()
        data = m.get_data()

        # TODO: how shall we do "genus" italics?

        # TODO: write stamp of last update to the template

        html = render_template('home/index.html', **locals())
        t.write(html, 'index')

    return t.read('index')

@home.route('/update')
def update():
    """
    fetch updates from modmine
    """
    return index(update=True)