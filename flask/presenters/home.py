#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Blueprint, render_template, request, redirect
from flask.helpers import url_for

# models
from models.modmine import Modmine

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('home/index.html', **locals())