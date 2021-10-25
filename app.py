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

@app.route("/")
def hello_world():
    return render_template("index.html")
