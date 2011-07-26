#!/usr/bin/python
# -*- coding: utf -*-

def slugify(value):
    import unicodedata, re

    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    return re.sub('[-\s]+', '-', value)

def fetch(url):
    import urllib2
    
    request = urllib2.Request(url)
    opener = urllib2.build_opener()
    r = opener.open(request)
    result = r.read()
    r.close()
    return result