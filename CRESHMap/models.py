"""Data models."""
from . import db
from geoalchemy2 import Geometry


URBAN_RURAL_CLASSIFICATION = ['UR2', 'UR3', 'UR6', 'UR8']


class Lookup(db.Model):
    __tablename__ = 'lookup'

    dz = db.Column(db.String(10), primary_key=True)
    iz = db.Column(db.String(10))
    mmward = db.Column(db.String(10))
    la = db.Column(db.String(10))
    spc = db.Column(db.String(10))
    ukpc = db.Column(db.String(10))
    hb = db.Column(db.String(10))
    hia = db.Column(db.String(10))
    spd = db.Column(db.String(10))
    sfrlso = db.Column(db.String(10))
    sfrsda = db.Column(db.String(10))
    rrp = db.Column(db.String(10))
    lrp = db.Column(db.String(10))
    ttwa = db.Column(db.String(10))
    ur2 = db.Column(db.Integer)
    ur3 = db.Column(db.Integer)
    ur6 = db.Column(db.Integer)
    ur8 = db.Column(db.Integer)


class GeographyTypes(db.Model):
    __tablename__ = 'cresh_geography_types'

    gss_code = db.Column(db.String(3), primary_key=True)
    name = db.Column(db.String())
    column_name = db.Column(db.String())

    geographies = db.relationship('Geography', backref='type')


class Geography(db.Model):
    __tablename__ = 'cresh_geography'

    gss_id = db.Column(db.String(10), primary_key=True)
    gss_code = db.Column(
        db.String(3), db.ForeignKey('cresh_geography_types.gss_code'))
    name = db.Column(db.String())
    geometry = db.Column(Geometry('GEOMETRY'))


class Variables(db.Model):
    __tablename__ = 'variables'

    id = db.Column(db.Integer, primary_key=True)
    variable = db.Column(db.String(), unique=True)
    domain = db.Column(db.String())
    description = db.Column(db.String())


class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    variable_id = db.Column(db.Integer, db.ForeignKey('variables.id'))
    gss_id = db.Column(db.String(10), db.ForeignKey('cresh_geography.gss_id'))
    year = db.Column(db.Integer)
    value = db.Column(db.Float)
