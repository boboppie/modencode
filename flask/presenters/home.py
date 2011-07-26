#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Blueprint, render_template, request, redirect
from flask.helpers import url_for

from libs.utils import write_template, read_template

# models
from models.modmine import Modmine

home = Blueprint('home', __name__)

@home.route('/')
def index(update=False):
    """
    serve home page
    """

    # TODO: force update on missing static html

    if update:
        # fetch data
        m = Modmine()
        data = m.get_data()

        # TODO: write stamp of last update to the template

        html = render_template('home/index.html', **locals())
        write_template(html, 'index')

    return read_template('index')

@home.route('/update')
def update():
    """
    fetch updates from modmine
    """
    index(update=True)