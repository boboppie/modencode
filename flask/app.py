#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Flask

# imports
import config

def create_app():
    # create our little application :)
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = config.SECRET_KEY

    # presenters
    from presenters.home import home

    # register modules
    app.register_blueprint(home)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=config.FLASK_PORT)