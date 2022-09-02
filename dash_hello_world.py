# imports
import dash
# import dash_html_components as html (deprecated)
from dash import html

# create (dash object) the app
app = dash.Dash(__name__)

# app layout
app.layout = html.Div([
    html.H1('Hello, World!')
])

# run app
if __name__ == '__main__':
    app.run_server(debug=True)
