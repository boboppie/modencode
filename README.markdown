A Flask app serving the homepage of the modENCODE project

## Requirements:
- Flask
- Flask-Mail (for sending mail from the contact form)
- CherryPy (for production)

## Installation:
- Make sure Flask <code>easy_install flask</code>, Flask-Mail <code>easy_install flask-mail</code> and CherryPy <code>easy_install cherrypy</code> are installed
- Run the install script <code>python install.py</code> and choose the port the app will run at
- Run the app, <code>python server.py</code>, or <code>python app.py</code> if you want to use the Werkzeug debugger and are on development

## Setup

- Configure SMTP and other settings in <code>config.py</code>, the docs are here [http://packages.python.org/Flask-Mail/#configuring-flask-mail](http://packages.python.org/Flask-Mail/#configuring-flask-mail)
- Modify site constants as needed in <code>models/constants.py</code>

## usage
- Visit <code>/update/</code> to fetch the latest data from modMine and update the homepage