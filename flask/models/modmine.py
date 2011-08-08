#!/usr/bin/python
# -*- coding: utf -*-

import config
from libs.utils import fetch
import json

class Modmine:

    catexp_ws_url = config.DATASOURCE_ROOT + 'service/query/metadatacache/catexp'
    webapp_path_ws_url = config.DATASOURCE_ROOT + 'service/query/metadatacache/webapp_path'

    #init value of metadata_cache is null
    metadata_catexp = None
    webapp_path = None

    def get_catexp_data(self, update=False):

        if update:
            Modmine.metadata_catexp = fetch(Modmine.catexp_ws_url)
        else:
            if not Modmine.metadata_catexp:
                Modmine.metadata_catexp = fetch(Modmine.catexp_ws_url)
            else:
                pass

        return json.loads(Modmine.metadata_catexp)

    def get_webapp_path(self, update=False):

        if update:
            Modmine.webapp_path = fetch(Modmine.webapp_path_ws_url)
        else:
            if not Modmine.webapp_path:
                Modmine.webapp_path = fetch(Modmine.webapp_path_ws_url)
            else:
                pass

        return Modmine.webapp_path