from __init__ import(
    db
)
from sqlalchemy.dialects.postgresql import UUID

class Nomnieki(db.Model):
    __table__ = db.Model.metadata.tables['Nomnieki']

class Nomas(db.Model):
    __table__ = db.Model.metadata.tables['Nomas']

class Kategorijas(db.Model):
    __table__ = db.Model.metadata.tables['Kategorijas']

class Produkti(db.Model):
    __table__ = db.Model.metadata.tables['Produkti']

class ProduktiNomas(db.Model):
    __table__ = db.Model.metadata.tables['ProduktiNomas']