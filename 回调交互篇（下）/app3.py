#而除了上面介绍的一股脑返回所有集合内成员部件的ALL模式之外，还有另一种更有针对性的MATCH模式，
# 它应用于结合内成员部件可交互输入值的情况，譬如下面这个简单的例子，我们定义一个简单的用于查询省份行政代码的应用，
# 配合MATCH模式来实现彼此成对独立输出：
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Container(
            [
                dbc.Row(
                    dbc.Col(
                        dbc.Button('新增查询', id='add-item', outline=True)
                    )
                ),
                html.Hr()
            ]
        ),
        dbc.Container([], id='query-container')
    ]
)

region2code = {
    '北京市': '110000000000',
    '重庆市': '500000000000',
    '安徽省': '340000000000'
}


@app.callback(
    Output('query-container', 'children'),
    Input('add-item', 'n_clicks'),
    State('query-container', 'children'),
    prevent_initial_call=True
)
def add_query_item(n_clicks, children):
    children.append(
        dbc.Row(
            [
                dbc.Col(
                    [
                        # 生成index相同的dropdown部件与文字输出部件
                        dcc.Dropdown(id={'type': 'select-province', 'index': children.__len__()},
                                     options=[{'label': label, 'value': label} for label in region2code.keys()],
                                     placeholder='选择省份：'),
                        html.P('请输入要查询的省份！', id={'type': 'code-output', 'index': children.__len__()})
                    ]
                )
            ]
        )
    )

    return children

@app.callback(
    Output({'type': 'code-output', 'index': MATCH}, 'children'),
    Input({'type': 'select-province', 'index': MATCH}, 'value')
)
def refresh_code_output(value):

    if value:
        return region2code[value]
    else:
        return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)