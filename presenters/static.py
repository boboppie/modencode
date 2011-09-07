#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Blueprint, render_template, redirect, url_for
import jinja2

# models
from models.constants import *

static = Blueprint('static', __name__)
    
@static.route('/<name>/')
def page(name):
    '''
    serve a 'static' page
    '''
    try:
    	return render_template('static/%s.html' % name, **globals())
    except jinja2.exceptions.TemplateNotFound:
    	return redirect(url_for('app.code_404'))