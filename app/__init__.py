from flask import Flask, render_template, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

import os

app = Flask(__name__) # create our application object
app.config.from_object('config') # load our local config file

heroku = Heroku(app) # create a heroku config object from our app object

login_manager = LoginManager(app) # create a LoginManager Object from our app object
bcrypt = Bcrypt(app)

db = SQLAlchemy(app) # create a db (SQLAlchemy) object from our app object

# register the users module blueprint
from app.users.views import mod as usersModule
app.register_blueprint(usersModule)

# add our view as the login view to finish configuring the LoginManager
login_manager.login_view = "users.login_view"

# assets bundling
from flask.ext.assets import Environment, Bundle
assets = Environment(app)
css_all = Bundle(
    'stylesheets/*.css',
    output='gen/application.css'
)
assets.register('css_all',css_all)

js_all = Bundle(
    'javascripts/main.js',
    output='gen/application.js'
)
assets.register('js_all',js_all)


# register the post module blueprint
from app.posts.views import mod as postsModule
app.register_blueprint(postsModule)

#----------------------------------------
# controllers
#----------------------------------------

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')
