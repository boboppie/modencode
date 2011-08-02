#!/usr/bin/python
# -*- coding: utf -*-

# server
from cherrypy import wsgiserver

# app
import app as flask
import config

app = flask.create_app()

d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', config.FLASK_PORT), d)

'''
better to print a message after server starts, not here?
'''
print "modENCODE is running on: http://localhost:%s" % config.FLASK_PORT, "...\n"

if __name__ == '__main__':
    try:
        server.start()        
    except KeyboardInterrupt:
        server.stop()
