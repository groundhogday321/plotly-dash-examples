# imports
import dash
from dash import html, dcc, Output, Input

# create (dash object) the apppy
app = dash.Dash(__name__)

# app layout
app.layout = html.Div([
    html.H1('INTERACTIVE TEXTBOX'),
    dcc.Input(id='input-text-box', value='type name here'),
    html.Div(id='text-box-output', style={'fontSize': 40})
])

# callback
@app.callback(
    Output(component_id='text-box-output', component_property='children'),
    Input(component_id='input-text-box', component_property='value'),
)
def updata_figure(input):
    return f'hello {input}'

# run app
if __name__ == '__main__':
    app.run_server(debug=True)