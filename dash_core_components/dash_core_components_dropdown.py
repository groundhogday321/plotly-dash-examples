# imports
import dash
from dash import html, dcc, Output, Input
import plotly.express as px

# data
gapminder = px.data.gapminder()
df = gapminder[gapminder['country'].isin(['United States', 'Spain', 'France', 'Nigeria', 'Chile'])]

# create (dash object) the app
app = dash.Dash(__name__)

# app layout
app.layout = html.Div([
    html.H1('INTERACTIVE CHART'),
    dcc.Dropdown(options=df.country.unique(), value='France', id='dropdown'),
    dcc.Graph(id='graph-with-dropdown')
])

# callback
@app.callback(
    Output(component_id='graph-with-dropdown', component_property='figure'),
    Input(component_id='dropdown', component_property='value'),
)
def updata_figure(country):
    filtered_df = df[df.country==country]
    fig = px.line(filtered_df, x='year', y='pop', title=f'Population of {filtered_df.country.unique()[0]}')
    return fig

# run app
if __name__ == '__main__':
    app.run_server(debug=True)