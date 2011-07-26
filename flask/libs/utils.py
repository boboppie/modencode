#!/usr/bin/python
# -*- coding: utf -*-

def slugify(value):
    import unicodedata, re

    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    return re.sub('[-\s]+', '-', value)

def fetch(url):
    # TODO: check the result status

    import urllib2
    
    request = urllib2.Request(url)
    opener = urllib2.build_opener()
    r = opener.open(request)
    result = r.read()
    r.close()
    return result

def write_template(template, name):
    # TODO: move to Template model

    import os

    with open(os.getcwd() + '/static/html/%s.html' % name, 'w') as f:
        f.write(template)

def read_template(name):
    # TODO: move to Template model

    import os
    
    with open(os.getcwd() + '/static/html/%s.html' % name, 'r') as f:
        html = f.read()
    return html