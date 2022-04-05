#Dash虽然很方便，使得我们可以完全不用书写js代码就可以实现各种回调交互，但把所有的交互响应计算过程都交给服务端来做，
# 省事倒是很省事，但会给服务器带来不小的计算和网络传输压力。
#因此很多容易频繁触发且与主要的数值计算无关的交互行为，完全可以搬到浏览器端执行，既快速又不吃服务器的计算资源，
# 这也是当初JavaScript被发明的一个重要原因，而在Dash中，也为略懂js的用户提供了在浏览器端执行一些回调的贴心功能。
#从一个很简单的点击按钮，实现部分网页内容的打开与关闭出发，这里我们提前使用到dbc.Collapse部件，
# 用于将所包含的网页内容与其它按钮部件的点击行为进行绑定：
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Button('服务端回调', id='server-button'),
            dbc.Collapse('服务端折叠内容', id='server-collapse'),
            html.Hr(),
            dbc.Button('浏览器端回调', id='browser-button'),
            dbc.Collapse('浏览器端折叠内容', id='browser-collapse'),
        ]
    )
)


@app.callback(
    Output('server-collapse', 'is_open'),
    Input('server-button', 'n_clicks'),
    State('server-collapse', 'is_open'),
    prevent_initial_call=True
)
def server_callback(n_clicks, is_open):
    return not is_open

# 在dash中定义浏览器端回调函数的特殊格式
app.clientside_callback(
    """
    function(n_clicks, is_open) {
        return !is_open;
    }
    """,
    Output('browser-collapse', 'is_open'),
    Input('browser-button', 'n_clicks'),
    State('browser-collapse', 'is_open'),
    prevent_initial_call=True
)

if __name__ == '__main__':
    app.run_server(debug=True)