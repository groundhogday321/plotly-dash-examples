# imports
import dash
from dash import html, dcc
import plotly.express as px

# data and chart prep
gapminder = px.data.gapminder()
india = px.data.gapminder().query("country=='India'")
us = px.data.gapminder().query("country=='United States'")
brazil = px.data.gapminder().query("country=='Brazil'")
# print(gapminder.head())

# create (dash object) the app
app = dash.Dash(__name__)

# markdown text
markdown_text = '''
This tutorial will go over examples of how to layout your app including using
html, css, markdown, core components (widgets), charts, and positioning on the page
'''

# app layout
app.layout = html.Div([
    # html, css
    html.H1('Hello World!', style={'color': 'orange', 'fontSize': 40}),

    # markdown
    dcc.Markdown(markdown_text),

    # core components
    dcc.Input(id='my-input', value='text box', type='text', style={'width': '335px', 'height': '35px', 'font-size': '35px'}),
    html.P('text box output goes here'),
    html.Br(),
    html.P('SLIDER'),
    dcc.Slider(0, 10, 1, value=5, id='slider_id'),
    html.P('slider output goes here'),
    html.Br(),
    html.P('DROPDOWN'),
    dcc.Dropdown(options=gapminder.country.unique(), value='India', id='dropdown_id'),
    # chart
    html.P('dropdown output (chart) below'),
    dcc.Graph(figure=px.line(india, x='year', y='lifeExp', title='Life expectancy in India')),

    # charts using css flexbox (side by side)
    # layout (side by side, size)
    # Create a folder named assets in the root of your app directory and include your CSS file in that folder. Dash will automatically serve all of the files that are included in this folder.
    html.P('CHARTS SIDE BY SIDE USING CSS FLEXBOX'),
    html.Div(
        className="container-1",
        children=[
            html.Div(
                dcc.Graph(figure=px.line(us, x="year", y="lifeExp", title='Life expectancy in US').update_layout(width=400))
                ),
            html.Div(
                dcc.Graph(figure=px.line(brazil, x="year", y="lifeExp", title='Life expectancy in Brazil').update_layout(width=400))
                ),
            html.Div(
                dcc.Graph(figure=px.line(india, x="year", y="lifeExp", title='Life expectancy in India').update_layout(width=400))
                ),
            ],style={'padding':50, 'border':'solid'}),
])

# run app
if __name__ == '__main__':
    app.run_server(debug=True)
