#!/usr/bin/python
# -*- coding: utf -*-

from libs.utils import fetch
import json

# models
from models.constants import *

class Modmine:

    catexp_ws_url = DATASOURCE_ROOT + '/service/query/metadatacache/catexp'
    webapp_path_ws_url = DATASOURCE_ROOT + '/service/query/metadatacache/webapp_path'
    gbrowse_base_url = DATASOURCE_ROOT + '/service/query/metadatacache/gbrowse_base_url'

    #init value of metadata_cache is null
    metadata_catexp = None
    webapp_path = None
    gbrowse_base = None

    def get_catexp_data(self):

        Modmine.metadata_catexp = fetch(Modmine.catexp_ws_url)

        # TODO check if returns json string
        return json.loads(Modmine.metadata_catexp)

    def get_webapp_path(self):

        Modmine.webapp_path = fetch(Modmine.webapp_path_ws_url)

        # TODO check if starts with "/"
        return Modmine.webapp_path

    def get_gbrowse_base(self):

        Modmine.gbrowse_base = fetch(Modmine.gbrowse_base_url)

        # TODO check if starts with "/"
        return Modmine.gbrowse_base