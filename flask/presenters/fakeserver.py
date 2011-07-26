#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Blueprint, jsonify

# fake data
from models.fakedata import data

modmine = Blueprint('modmine', __name__)

@modmine.route('/modmine/gimme/fake/data')
def serve():
    """
    A fake modmine server serving fake data to display on the modmine homepage
    """
    return jsonify(data)