from __init__ import(
    db
)
from sqlalchemy.dialects.postgresql import UUID

NomniekiModel = db.Model.metadata.tables['Nomnieki']
NomasModel = db.Model.metadata.tables['Nomas']
ProduktiModel = db.Model.metadata.tables['Produkti']
ProduktiNomasModel = db.Model.metadata.tables['ProduktiNomas']
KategorijasModel = db.Model.metadata.tables['Kategorijas']
print(type(ProduktiModel))
Nomnieki = db.Table('Nomnieki', db.metadata, autoload_with=db.engine)
Nomas = db.Table('Nomas', db.metadata, autoload_with=db.engine)
Kategorijas = db.Table('Kategorijas', db.metadata, autoload_with=db.engine)
Produkti = db.Table('Produkti', db.metadata, autoload_with=db.engine)
ProduktiNomas = db.Table('ProduktiNomas', db.metadata, autoload_with=db.engine)
print(type(Produkti))