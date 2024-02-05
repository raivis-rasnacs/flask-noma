from flask import Flask, render_template, request, url_for, redirect

from config import Config
from __init__ import create_app

app = create_app()

import views

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.add_url_rule('/', 
    view_func=views.home)
app.add_url_rule('/produkti', 
    view_func=views.produkti)
app.add_url_rule('/jauns-produkts', 
    view_func=views.jauns_produkts)
app.add_url_rule('/kategorijas', 
    view_func=views.kategorijas)
app.add_url_rule('/nomas', 
    view_func=views.nomas)
app.add_url_rule('/jauna-noma', 
    view_func=views.jauna_noma)
app.add_url_rule('/nomnieki', 
    view_func=views.nomnieki)
app.add_url_rule('/jauns-nomnieks', 
    view_func=views.jauns_nomnieks)

if __name__ == '__main__':
    if app.config['FLASK_ENVIRONMENT'] == 'development':
        app.run(debug=True)
