#!/usr/bin/python
# -*- coding: utf -*-

import config
from libs.utils import fetch
import json

class Modmine:

    fly_catexp_url = config.DATASOURCE_ROOT + 'service/query/metadatacache?org=fly&type=metadatacach_catexp'
    worm_catexp_url = config.DATASOURCE_ROOT + 'service/query/metadatacache?org=worm&type=metadatacach_catexp'

    #init value of metadata_cache is null
    metadata_fly_catexp = None
    metadata_worm_catexp = None

    def get_fly_catexp_data(self):

        if not Modmine.metadata_fly_catexp:
            Modmine.metadata_fly_catexp = fetch(Modmine.fly_catexp_url)
        else:
            pass

        return json.loads(Modmine.metadata_fly_catexp)

    def get_worm_catexp_data(self):

        if not Modmine.metadata_worm_catexp:
            Modmine.metadata_worm_catexp = fetch(Modmine.worm_catexp_url)
        else:
            pass

        return json.loads(Modmine.metadata_worm_catexp)