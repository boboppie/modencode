#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Blueprint, render_template

# models
from models.constants import *

static = Blueprint('static', __name__)
    
@static.route('/<name>')
def page(name):
    '''
    serve a 'static' page
    '''
    return render_template('static/%s.html' % name, **globals())