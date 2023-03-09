# -*- coding: utf-8 -*-
from app import db



class IndianGdp(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gdp_usd = db.Column(db.Integer, nullable=False)
    gdp_year = db.Column(db.Integer, nullable=False)
