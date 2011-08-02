#!/usr/bin/python
# -*- coding: utf -*-

import config
from libs.utils import fetch
import json

class Modmine:

    ''' init value of metadata_cache is null '''
    metadata_cache = None

    def get_data(self):
        # TODO: replace with an actual call to modmine
        if not Modmine.metadata_cache:
            Modmine.metadata_cache = fetch('http://localhost:%i/modmine/gimme/fake/data' % config.FLASK_PORT)
        else:
            pass

        return json.loads(Modmine.metadata_cache)
