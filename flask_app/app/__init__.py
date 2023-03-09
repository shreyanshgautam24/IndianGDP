# -*- coding: utf-8 -*-
from app.config import Config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path="/app/static")
app.debug = True
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import models, routes  # noqa

app.register_blueprint(routes.indiangdp, url_prefix="/")  # noqa


# from app.models import IndianGdp


# for indx, gdp in enumerate([283.75,299.65,300.19,326.61,274.84,293.26,284.19,333.01,366.60,399.79,423.19,428.77,466.84,476.64,493.93,523.77,618.37,721.59,834.22,949.12,1238.70,1224.10,1365.37,1708.46,1823.05,1827.64,1856.72,2039.13,2103.59,2294.12,2651.47,2702.93,2831.55,2667.69,3176.30,3468.57,3820.57,4170.22,4547.16,4947.39,5365.55]):
#     india = IndianGdp(
#             gdp_usd=gdp,
#             gdp_year=1987+indx
#         )
#     db.session.add(india)
#     db.session.commit()