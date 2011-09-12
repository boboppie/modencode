#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Blueprint, render_template, redirect, url_for
import jinja2

# models
from models.constants import *

static = Blueprint('static', __name__)
    
@static.route('/<name>/')
@static.route('/publications/<name>/')
@static.route('/publications/<name>/index.shtml')
def page(name):
    '''
    serve a 'static' page
    '''
    try:
    	return render_template('static/%s.html' % name, **globals())
    except jinja2.exceptions.TemplateNotFound:
    	return redirect(url_for('app.code_404'))

@static.route('/publications/integrative_fly_2010/')
@static.route('/publications/integrative_fly_2010/index.shtml')
def fly_page():
	return redirect(url_for('static.page', name='fly_2010pubs'))

@static.route('/publications/integrative_worm_2010/')
@static.route('/publications/integrative_worm_2010/index.shtml')
def worm_page():
	return redirect(url_for('static.page', name='worm_2010pubs'))

@static.route('/publications/files/<first>')
@static.route('/publications/files/<first>/<second>')
def file(first, second=None):
	if second:
		return redirect('%s/%s/%s' % (FILES_URL, first, second))
	return redirect('%s/%s' % (FILES_URL, first))