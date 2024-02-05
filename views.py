from flask import (
    request,
    render_template,
    redirect,
    url_for
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
            else:
                pieejams = False
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

def nomas():
    if request.method == "POST":
        pass
    else:
        nomas = db.session.query(Nomas, Nomnieki).join(Nomnieki).all()
        return render_template(
            "nomas.html", 
            nomas=nomas
        )
    
def jauna_noma():
    if request.method == "POST":
        sak_dat = request.form.get("sak-dat")
        beigu_dat = request.form.get("beigu-dat")
        nomnieks = request.form.get("nomnieks")
        produkti = request.form.get("produkti")
    else:
        nomas = db.session.query(Nomas, Nomnieki).join(Nomnieki).all()
        produkti = db.session.query(Produkti).all()
        nomnieki = db.session.query(Nomnieki).all()
        return render_template(
            "jauna_noma.html", 
            nomas=nomas,
            produkti=produkti,
            nomnieki=nomnieki
        )
jauna_noma.methods = ["GET", "POST"]
    
def nomnieki():
    nomnieki = db.session.query(Nomnieki).all()
    return render_template("nomnieki.html", nomnieki=nomnieki)

def jauns_nomnieks():
    if request.method == "POST":
        vards = request.form.get("vards")
        uzvards = request.form.get("uzvards")
        pers_kods = request.form.get("personas-kods")
        tel_numurs = request.form.get("tel-numurs")

        jauns_nomnieks = Nomnieki(
                nomnieka_id=str(uuid4()),
                vards=vards,
                uzvards=uzvards,
                pers_kods=pers_kods,
                tel_numurs=tel_numurs
            )
        db.session.add(jauns_nomnieks)
        db.session.commit()
        return redirect("/jauns-nomnieks")
    else:
        return render_template(
            "jauns_nomnieks.html"
        )
jauns_nomnieks.methods = ["GET", "POST"]