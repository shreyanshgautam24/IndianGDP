# -*- coding: utf-8 -*-
from flask import Blueprint, redirect, render_template, request
from io import BytesIO
import base64
import mpld3
import matplotlib.pyplot as plt
import numpy as np
from app.models import IndianGdp
import plotly
import plotly.graph_objs as go
import pandas as pd
import plotly.io as pio
import plotly.express as px
import requests
from requests.adapters import HTTPAdapter, Retry
import json
import ast



indiangdp = Blueprint(
    "indiangdp", __name__, template_folder="templates"
)

@indiangdp.route("/", methods=["GET", "POST"])
def base(task=None):
    gdp = []
    year = []
    indian_gdp_figures = IndianGdp.query.all()
    for indian in indian_gdp_figures:
        gdp.append(indian.gdp_usd)
        year.append(indian.gdp_year)
    if request.method == 'POST':
        adapter = HTTPAdapter(max_retries=1)
        http = requests.Session()
        http.mount("https://", adapter)
        http.mount("http://", adapter)
        url = 'https://api.currencyfreaks.com/latest?apikey=c9497a59247c4bfc8589d9243738a604'
        request_data = http.get(url)
        content = json.loads(request_data.content.decode("UTF-8"))
        latest_inr_rates = content.get('rates').get('INR')
        gdp = [usd*float(latest_inr_rates) for usd in gdp]
    df = pd.DataFrame({
      'gdp': gdp,
      'year': year
    })
    fig = px.line(df, x='year', y='gdp')
    fig.update_layout(xaxis_tickvals=year)
    fig.add_trace(
    go.Scatter(
        x=year,
        y=gdp,
        mode='lines+markers',  # Add the 'markers' mode to show markers
        marker=dict(
            size=10,
            color='blue',
            symbol='circle',
            line=dict(width=1),
        ),
        line=dict(
            color='blue',
            width=2,
            dash='dash'
        )
    )
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template(
        "base.html",
        graphJSON=graphJSON
    )


   

