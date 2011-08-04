#!/usr/bin/python
# -*- coding: utf -*-

import config
from libs.utils import fetch
import json

class Modmine:

    catexp_url = config.DATASOURCE_ROOT + 'service/query/metadatacache?datatype=metadatacach_catexp'

    #init value of metadata_cache is null
    metadata_catexp = None

    def get_catexp_data(self):

        if not Modmine.metadata_catexp:
            Modmine.metadata_catexp = fetch(Modmine.catexp_url)
        else:
            pass

        return json.loads(Modmine.metadata_catexp)