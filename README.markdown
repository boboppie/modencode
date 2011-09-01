This is Fengyuan's fork from Radek's original project @ git://github.com/radekstepan/modencode.git

A Flask app serving the homepage of the modENCODE project

## Requirements:
- Flask
- CherryPy

## Installation:
- Make sure Flask is installed, <code>easy_install flask</code>, to install the bleeding edge version, refer to http://flask.pocoo.org/docs/installation/#living-on-the-edge
- Make sure CherryPy is installed, <code>easy_install cherrypy</code>
- Run the install script <code>python install.py</code> and input the port the app will run at
- Run the app, <code>python server.py</code>

## Usage:

- Visit <code>/update</code> to force an update to html cache
- Change modMine webservice base url in install.py (DATASOURCE_ROOT field), and install the script again 
