#!/usr/bin/python
# -*- coding: utf -*-

import os

class Templates:

    def __init__(self, name):
        self.path = os.getcwd() + '/static/html/%s.html' % name

    def exists(self):
        """
        check that a file exists
        """
        return os.path.isfile(self.path)

    def write(self, template):
        """
        write html into a template file
        """
        with open(self.path, 'w') as f:
            f.write(template)

    def read(self):
        """
        read html from a template file
        """
        with open(self.path, 'r') as f:
            html = f.read()
        return html
