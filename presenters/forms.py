#!/usr/bin/python
# -*- coding: utf -*-

import config

# framework
from flask import Blueprint, render_template, request, redirect, url_for

# email
import libs.mail

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
    fail = {}
    if request.method == 'POST':
        if not 'email' in request.form or len(request.form['email']) < 1: fail['email'] = 'Please enter an email address'
        if not 'message' in request.form or len(request.form['message']) < 1: fail['message'] = 'Please fill in this field'
        if not fail:
            # form msg
            message_body = "From %s%s:\n\n%s" %\
                (request.form['email'], " (%s)" % request.form['name'] if len(request.form['name']) > 0 else '', request.form['message'])
            
            # send
            try:
                result = libs.mail.send(request.form['email'], message_body)
                if result:
                    raise Exception()
                
                message = { 'class':'success', 'text':'Your message has been <strong>sent</strong>.' }
            except:
                message = { 'class':'fail', 'text':'There was a problem sending your message, try to email us directly'\
                ' at <strong><a href="mailto:%s">%s</a></strong>.' % (config.MAIL_RECIPIENTS[0], config.MAIL_RECIPIENTS[0]) }

    return render_template('forms/contact.html', **dict(locals().items() + globals().items()))