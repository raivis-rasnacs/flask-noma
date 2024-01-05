from flask import (
    request,
    render_template,
    redirect
)
from models import (
    Nomas,
    Nomnieki,
    Produkti,
    ProduktiNomas,
    Kategorijas
)
from __init__ import db
from uuid import uuid4

def home():
    return render_template("home.html")
home.methods = ["GET"]

def produkti():
    produkti = Produkti.query.all()
    #produkti = db.session.query(NomniekiModel).all()
    print(produkti)
    return render_template("home.html")
produkti.methods = ["GET"]

def kategorijas():
    if request.method == "POST":
        method = request.form.get("_method")
        if method == "PUT":
            nosaukums = request.form.get("nosaukums")
            jauna_kateg = Kategorijas(
                kateg_id=str(uuid4()),
                nosaukums=nosaukums)
            db.session.add(jauna_kateg)
            db.session.commit()
            return redirect("kategorijas")
    else:
        kategorijas = Kategorijas.query.all()
        for kategorija in kategorijas:
            print(kategorija.nosaukums)
        return render_template("kategorijas.html", kategorijas=kategorijas)
kategorijas.methods = ["GET", "POST"]
