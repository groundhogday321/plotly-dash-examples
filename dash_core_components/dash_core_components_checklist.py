# imports
import dash
from dash import html, dcc, Output, Input
import plotly.express as px
from vega_datasets import data as vds

# data
airports = vds.airports()[0:15]

# create (dash object) the app
app = dash.Dash(__name__)

# app layout
app.layout = html.Div([
    html.H1('INTERACTIVE CHECKLIST'),
    dcc.Checklist(options=airports.name.unique(), value=['Perry-Warsaw'], id='checklist'),
    dcc.Graph(id='map')
])

# callback
@app.callback(
    Output(component_id='map', component_property='figure'),
    Input(component_id='checklist', component_property='value'),
)
def updata_figure(airports_selected):
    filtered_airports = airports[airports['name'].isin(airports_selected)]
    fig = px.scatter_geo(filtered_airports, lat=filtered_airports.latitude, lon=filtered_airports.longitude, projection='natural earth', hover_name=filtered_airports.name, hover_data=['state'])
    fig.update_layout(autosize=False, width=800, height=800)
    fig.update_geos(projection_scale=4, center_lat=38, center_lon=-98) 
    return fig

# run app
if __name__ == '__main__':
    app.run_server(debug=True)