#!/usr/bin/python
# -*- coding: utf -*-

import config
from libs.utils import fetch
import json

class Modmine():

    def get_data(self):
        """
        Fetch available data from modmine
        """

        # TODO: replace with an actual call to modmine

        r = fetch('http://localhost:%i/modmine/gimme/fake/data' % config.FLASK_PORT)
        return json.loads(r)