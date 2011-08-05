#!/usr/bin/python
# -*- coding: utf -*-

import os

class Templates():

    def __init__(self, name):
        self.dir = os.getcwd() + '/static/html/'
        self.path = self.dir + '%s.html' % name

    def exists(self):
        """
        check that a file exists
        """
        return os.path.isfile(self.path)

    def write(self, template):
        """
        write html into a template file
        """
        if not os.path.isdir(self.dir):
            os.makedirs(self.dir)

        with open(self.path, 'w') as f:
            f.write(template)

    def read(self):
        """
        read html from a template file
        """
        with open(self.path, 'r') as f:
            html = f.read()
        return html