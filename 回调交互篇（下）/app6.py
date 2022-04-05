# 下面我们直接以大家喜闻乐见的数据可视化顶级框架echarts为例，来写一个根据不同输入值切换渲染出的图表类型，
# 注意请从官网把依赖的echarts.min.js下载到我们的assets路径下对应位置，它会在我们的Dash应用启动时与所有assets下的资源
# 一起自动被载入到浏览器中
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, ClientsideFunction

app = dash.Dash(__name__)

# 编写一个根据dropdown不同输入值切换对应图表类型的小应用
app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            dbc.Row(
                dbc.Col(
                    dcc.Dropdown(
                        id='chart-type',
                        options=[
                            {'label': '折线图', 'value': '折线图'},
                            {'label': '堆积面积图', 'value': '堆积面积图'},
                        ],
                        value='折线图'
                    ),
                    width=3
                )
            ),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    html.Div(
                        html.Div(
                            id='main',
                            style={
                                'height': '100%',
                                'width': '100%'
                            }
                        ),
                        style={
                            'width': '800px',
                            'height': '500px'
                        }
                    )
                )
            )
        ]
    )
)

app.clientside_callback(
    # 关联自编js脚本中的相应回调函数
    ClientsideFunction(
        namespace='clientside',
        function_name='switch_chart'
    ),
    Output('main', 'children'),
    Input('chart-type', 'value')
)

if __name__ == '__main__':
    app.run_server(debug=True)