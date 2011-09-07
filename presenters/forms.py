#!/usr/bin/python
# -*- coding: utf -*-

import config

# framework
from flask import Blueprint, render_template, request, redirect, url_for

# models
from models.constants import *

forms = Blueprint('forms', __name__)

@forms.route('/contact/', methods=['GET', 'POST'])
@forms.route('/contacts/', methods=['GET', 'POST'])
@forms.route('/contact-us/', methods=['GET', 'POST'])
def contact():
    """
    contact form, duh
    """
    if request.method == 'POST':
        return "POST"

    return render_template('forms/contact.html', **dict(locals().items() + globals().items()))