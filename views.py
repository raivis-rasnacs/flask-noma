from flask import (
    request,
    render_template,
    redirect
)
from models import (
    NomasModel,
    NomniekiModel,
    ProduktiModel,
    ProduktiNomasModel,
    KategorijasModel
)
from __init__ import db

def home():
    return render_template("home.html")
home.methods = ["GET"]

def show_produkti():
    #produkti = ProduktiModel.query.all()
    produkti = db.session.query(NomniekiModel).all()
    print(produkti)
    return render_template("home.html")
show_produkti.methods = ["GET"]