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
from sqlalchemy.orm import joinedload

def home():
    return render_template("home.html")
home.methods = ["GET"]

def produkti():
    if request.method == "POST":
        method = request.form.get("_method")
        if method == "PUT":
            nosaukums = request.form.get("nosaukums")
            kateg_id = request.form.get("kategorija")
            teh_rakst = request.form.get("teh_rakst")
            pieejams = request.form.get("pieejams")
            if pieejams is not None:
                pieejams = True
            dienas_cena = request.form.get("dienas_cena")
            
            jauns_produkts = Produkti(
                produkta_id=str(uuid4()),
                nosaukums=nosaukums,
                kateg_id=kateg_id,
                teh_rakst=teh_rakst,
                pieejams=pieejams,
                dienas_cena=dienas_cena
            )
            db.session.add(jauns_produkts)
            db.session.commit()

            return redirect("produkti")
    else:
        produkti = db.session.query(Produkti, Kategorijas).join(Kategorijas).all()
        kategorijas = Kategorijas.query.all()
        return render_template(
            "produkti.html", 
            produkti=produkti,
            kategorijas=kategorijas)
produkti.methods = ["GET", "POST"]

def jauns_produkts():
    if request.method == "POST":
        pass
    else:
        kategorijas = Kategorijas.query.all()
        return render_template(
            "jauns_produkts.html", 
            kategorijas=kategorijas)
jauns_produkts.methods = ["GET", "POST"]

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
        return render_template(
            "kategorijas.html", 
            kategorijas=kategorijas)
kategorijas.methods = ["GET", "POST"]
