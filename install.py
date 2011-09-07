#!/usr/bin/python
# -*- coding: utf -*-

import random, os

# config settings to save
cfg = {
    'FLASK_PORT' : 5000,
    'DEBUG' : False,
    'SECRET_KEY' : '',
    'ALLOWED_IP' : ['127.0', '192.168']
}

# flask app port
while True:
    input_port = raw_input('Flask app port (default 5000) ')

    if not input_port:
        cfg['FLASK_PORT'] = 5000
        break

    if input_port:
        cfg['FLASK_PORT'] =  int(input_port.strip()) # Better to use Regex to contraint this
        break

cfg['SECRET_KEY'] = ''.join([random.choice('./ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for i in range(30)])

python_code = []
for key, value in cfg.items():
    if isinstance(value, str):
        value = "'" + value.replace("'", r"\'") + "'"
    python_code.append("%s = %s" % (key, value))

with open(os.getcwd() + '/config.py', 'w') as f:
    f.write('\n'.join(python_code))

print('\nConfiguration file written successfully.\n')