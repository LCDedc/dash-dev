# 单选框和复选框
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
import json

app = dash.Dash(__name__)

app.layout=html.Div(
    dbc.Container(
        [
            dbc.Checklist (#RadioItems是单选
                id='check-list-input',
                inline=True,
                switch=True,
                options=[
                    {'label':item,'value':item}
                    for item in list("ABCD")
                ],
                style={'width':'300px'}
            ),
            html.P(id='check-list-output')
        ],
        style={'margin-top':'100px'}
    )
)
@app.callback(
    Output('check-list-output','children'),
    Input('check-list-input','value')
)

def check_list_output(value):
    if value:
        return '已选择'+'、'.join(value)
    return dash.no_update

if __name__=="__main__":
    app.run_server(debug=True)