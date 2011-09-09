#!/usr/bin/python
# -*- coding: utf -*-

import config
import smtplib
 
def send(from_address, message):
 	# form the message
	message = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (
		from_address,
		','.join(config.MAIL_RECIPIENTS),
		'modENCODE Contact Form',
		message)

    # SMTP server
	server = smtplib.SMTP(host=config.MAIL_SERVER, port=config.MAIL_PORT, timeout=10)

	# use TLS?
	if config.MAIL_USE_TLS:
		server.ehlo()
		server.starttls()
		server.ehlo()
	
	# login
	server.login(config.MAIL_USERNAME, config.MAIL_PASSWORD)

	# send & quit
	problems = server.sendmail(from_address, config.MAIL_RECIPIENTS, message)
	server.quit()

	return problems