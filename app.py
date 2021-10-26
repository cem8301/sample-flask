#!/usr/bin/env python3
from flask import Flask, render_template, request
import requests
import pandas as pd
from pandas.tseries.offsets import *
import pandas as pd
from flatten_dict import flatten
from stravalib import Client
import polyline
import os
import json
import datetime
import urllib.parse
import dash
import dash_html_components as html
import dash_leaflet as dl
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate
from dotenv import load_dotenv

load_dotenv()
server = Flask(__name__)
app = dash.Dash(
    __name__,
    server=server
)
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    html.A("Get Some Data!",
           href="https://www.strava.com/oauth/authorize?client_id=32737&response_type=code&redirect_uri=https://www.giraffesinaboat.com/exchange_token&approval_prompt=force&scope=activity:read_all")
])


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname'),
     Input('url', 'href')]
)
def display_page(pathname, href):
    return index_page

if __name__ == "__main__":
    app.run_server(debug=True,host='0.0.0.0')
