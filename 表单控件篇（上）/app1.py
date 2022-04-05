# 输入框部件
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            dbc.Input(id='input-text',
                      placeholder="text模式，长度限制4",
                      type='text',
                      maxLength=4,
                      style={'width': '300px'}),
            html.P(id='output-text'),
            dbc.Input(id='input-password',
                      placeholder='password模式，绑定Enter键',
                      type='password',
                      style={'width': '300px'},
                      debounce=True),
            html.P(id='output-password'),
            dbc.Input(id='input-seaech',
                      placeholder='search模式，可快速清除内容',
                      type='serch',
                      style={'width': '300px'}),
            html.P(id='output-search')
        ],
        style={"margin-top": "100px"}
    )
)


@app.callback(
    Output('output-text', 'children'),
    Input('input-text', 'value')
)
def output_text(value):
    return value


@app.callback(
    Output('output-password', 'children'),
    [Input('input-password', 'value'),
     Input('input-password', 'n_submit')]
)
def output_password(value, n_submit):
    if value:
        return '密码为：' + value + f'第{n_submit}次按下Enter'
    return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)
