#!/usr/bin/python
# -*- coding: utf -*-

import config

# flask extension
from flaskext.mail import Mail    

mail = None

def init_mail(app):
	global mail

	mail = Mail()
	mail.init_app(app)