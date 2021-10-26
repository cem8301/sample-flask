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

local_timezone = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
dend = pd.Timestamp.today() + pd.DateOffset(years=1)
datelist = pd.date_range(start='1/1/2009', end= dend, freq='Y', tz=local_timezone)
maxmarks = len(datelist) - 1
DLIST = pd.DatetimeIndex(datelist).normalize()
TAGS = {}
for idx,item in enumerate(DLIST):
    TAGS[idx] = (item + DateOffset(months=1)).strftime('%Y')

page_1_layout = html.Div([
    dcc.Loading(
        id="loading-1",
        type="default",
        fullscreen=True,
        children=[html.Div(dcc.Store(id='memory')),
                  html.Div(dcc.Store(id='local', storage_type='local')),
                  html.Div(dcc.Store(id='session', storage_type='session')),
                  html.Div(dcc.Dropdown(
                           id='dropdown',
                           multi=True,
                           placeholder="Select Activity Type")),
                  html.Div(dcc.Dropdown(
                           id='dropdown2',
                           multi=True,
                           placeholder="Select Gear"
                  )),
                  html.Div(dcc.RangeSlider(
                           id='time-slider',
                           updatemode='mouseup',
                           count=1,
                           min=0,
                           max=maxmarks,
                           step=1,
                           value=[0,maxmarks],
                           marks=TAGS,
                           pushable=1
                  ))]
    ),
    html.Div(id='test',
             style={'width': '100%',
                    'height': '600px',
                    'margin': 'auto',
                    'display': 'block'})
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname'),
     Input('url', 'href')]
)
def display_page(pathname, href):
    if pathname == '/exchange_token':
        return page_1_layout
    else:
        return index_page

