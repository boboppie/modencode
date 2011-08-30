#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Flask

# imports
import config

# utils
import re, unicodedata, urllib, time

app = None

def create_app():
    global app

    # create our little application :)
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = config.SECRET_KEY
    app.debug = False

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
        # TODO: this should be done on a server level or in the model!
        organisms = []
        for organism in list_of_organism_experiments:
            if len(organism['experiments']) > 0:
                organisms.append(organism)
        return organisms

    @app.template_filter('slugify')
    def slugify(value):
        """
        Slugify an input text (Django style)
        """
        if isinstance(value, unicode):
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
        value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
        return re.sub('[-\s]+', '-', value)

    @app.template_filter('url_encode')
    def url_encode(uri):
        return urllib.quote_plus(uri)

    @app.template_filter('article_image')
    def article_image(article):
        """
        Determine article image name
        """
        return slugify('-'.join([article['journal'], article['vol'], article['date']]))

    @app.template_filter('shorten_authors')
    def shorten_authors(authors, title, limit=140):
        """
        Shorten the authors listing if too long
        """
        limit -= len(title)
        result = []
        for author in authors.split(', '):
            limit -= len(author)
            result.append(author)
            if limit < 0: break
        return ', '.join(result) + '&hellip;' if limit < 0 else ', '.join(result)

    @app.template_filter('flatten_publications')
    def flatten_publications(pubs):
        """
        Make a dict into a list of individual articles with journal field
        """
        articles = []
        for journal in pubs['journal']:
            for article in journal['articles']:
                article['journal'] = journal['name']
                articles.append(article)
        return sorted(articles,
                      key=lambda a: time.mktime(time.strptime(a['date'], "%d %B %Y" if len(a['date'].split()) == 3 else "%B %Y")),
                      reverse=True)

    @app.template_filter('italics')
    def italics(text):
        """
        Apply italics to genus etc.
        """
        return re.sub(re.compile('('+('|'.join(['C\. elegans', 'Caenorhabditis elegans', 'D\. melanogaster', 'Drosophila melanogaster',
        'Drosophila', 'cis-', 'trans-']))+')'), lambda m: "<i>%s</i>" % m.group(1), text)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=config.FLASK_PORT)