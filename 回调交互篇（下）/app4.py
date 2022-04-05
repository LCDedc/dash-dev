#在很多应用场景下，我们的某个回调可能拥有多个Input输入，但学过前面的内容我们已经清楚，
# 不管有几个Input，只要其中有一个部件其输入属性发生变化，都会触发本轮回调，
# 但是如果我们就想知道究竟是哪个Input触发了本轮回调该怎么办呢？
#这在Dash中可以通过dash.callback_context来方便的实现，它只能在回调函数中被执行，从而获取回调过程的诸多上下文信息，
# 先从下面这个简单的例子出发看看dash.callback_context到底给我们带来了哪些有价值的信息：
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import json

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dbc.Button('A', id='A', n_clicks=0)),
                    dbc.Col(dbc.Button('B', id='B', n_clicks=0)),
                    dbc.Col(dbc.Button('C', id='C', n_clicks=0))
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(html.P('按钮A未点击', id='A-output')),
                    dbc.Col(html.P('按钮B未点击', id='B-output')),
                    dbc.Col(html.P('按钮C未点击', id='C-output'))
                ]
            ),
            dbc.Row(
                dbc.Col(
                    html.Pre(id='raw-json')
                )
            )
        ]
    )
)


@app.callback(
    [Output('A-output', 'children'),
     Output('B-output', 'children'),
     Output('C-output', 'children'),
     Output('raw-json', 'children')],
    [Input('A', 'n_clicks'),
     Input('B', 'n_clicks'),
     Input('C', 'n_clicks')],
    prevent_initial_call=True
)
def refresh_output(A_n_clicks, B_n_clicks, C_n_clicks):

    # 获取本轮回调状态下的上下文信息
    ctx = dash.callback_context

    # 取出对应State、最近一次触发部件以及Input信息
    ctx_msg = json.dumps({
        'states': ctx.states,
        'triggered': ctx.triggered,
        'inputs': ctx.inputs
    }, indent=2)

    return A_n_clicks, B_n_clicks, C_n_clicks, ctx_msg

if __name__ == '__main__':
    app.run_server(debug=True)