# imports
import dash
from dash import html, dcc, Output, Input
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
# import base64
from base64 import b64decode
from io import BytesIO

# model
model = ResNet50(weights='imagenet')

# create (dash object) the app
app = dash.Dash(__name__)

# app layout
app.layout = html.Div([
    html.H1('DRAG AND DROP'),
    html.H2('Identify Image'),
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '50%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
    ),
    html.P('The image is most likely one of the following:'),
    html.Div(id='prediction', style={'fontSize': 40, 'color': 'blue'}),
])

# callback
@app.callback(
    Output(component_id='prediction', component_property='children'),
    Input(component_id='upload-image', component_property='contents'),
)
def make_prediction(image_to_predict):
    if image_to_predict is not None:
        # load image to predict
        img = image.load_img(BytesIO(b64decode(image_to_predict.split(',')[1])), target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        prediction = model.predict(x)
        make_prediction = decode_predictions(prediction)
        # display prediction(s)
        print(make_prediction)                
        return f'{make_prediction[0][0][1]} or {make_prediction[0][1][1]}'

# run app
if __name__ == '__main__':
    app.run_server(debug=True)