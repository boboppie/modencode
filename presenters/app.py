#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Blueprint, render_template, request, redirect, url_for

app = Blueprint('app', __name__)

@app.route('/401/<ip>/')
def code_401(ip):
    return render_template('app/401.html', ip=ip)

@app.route('/404/')
def code_404():
    return render_template('app/404.html')