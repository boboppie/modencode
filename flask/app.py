#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Flask

# imports
import config
import libs.filters

app = None

def create_app():
    global app

    # create our little application :)
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = config.SECRET_KEY

    # presenters
    from presenters.home import home
    from presenters.fakeserver import modmine

    # register modules
    app.register_blueprint(home)
    app.register_blueprint(modmine)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=config.FLASK_PORT)