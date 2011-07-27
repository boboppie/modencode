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
    t = Templates('index')

    if update or not t.exists():
        # fetch data
        m = Modmine()
        data = m.get_data()

        # TODO: how shall we do "genus" italics?

        # TODO: write stamp of last update to the template

        html = render_template('home/index.html', **locals())
        t.write(html)

    return t.read()

@home.route('/update')
def update():
    """
    fetch updates from modmine
    """
    return index(update=True)