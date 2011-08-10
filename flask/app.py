#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Flask

# imports
import config

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

    # template filters
    @app.template_filter('pi_filter')
    def pi_filter(list_of_experiments):
        """
        Give a unique list of pis for a category organism
        """
        pis = []
        for exp in list_of_experiments:
            if exp['pi'] not in pis:
                pis.append(exp['pi'])
        return pis

    @app.template_filter('empty_organisms_filter')
    def empty_organisms_filter(list_of_organism_experiments):
        """
        Make sure that empty experiments do not get processed
        """
        organisms = []
        for organism in list_of_organism_experiments:
            if len(organism['experiments']) > 0:
                organisms.append(organism)
        return organisms

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=config.FLASK_PORT)