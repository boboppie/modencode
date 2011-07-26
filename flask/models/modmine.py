#!/usr/bin/python
# -*- coding: utf -*-

import config
from libs.utils import fetch
import json

class Modmine():

    def update_data(self):
        """
        Fetch available data from modmine
        """
        r = fetch('http://localhost:%i/modmine/gimme/fake/data' % config.FLASK_PORT)
        data = json.loads(r)