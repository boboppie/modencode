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
        r = fetch('http://intermine.modencode.org/modminetest/service/query/metadatacache/catexp')
        return json.loads(r)