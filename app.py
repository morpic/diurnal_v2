import dash
import pandas as pd
from dash import Dash, dash_table, dcc, html, Input, Output, State
import plotly.express as px

app = Dash(__name__)
server = app.server

if __name__ == "__main__":
    app.run_server()
