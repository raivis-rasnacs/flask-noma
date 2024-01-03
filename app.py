from flask import Flask, render_template, request, url_for, redirect

from config import Config
from __init__ import create_app

app = create_app()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

with app.app_context():
    import views

app.add_url_rule('/', 
    view_func=views.home)
app.add_url_rule('/produkti', 
    view_func=views.show_produkti)

if __name__ == '__main__':
    if app.config['FLASK_ENVIRONMENT'] == 'development':
        app.run(debug=True)
