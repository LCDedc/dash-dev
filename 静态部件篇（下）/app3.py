#以Tabs来组织Tab子元素
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app=dash.Dash(__name__)

app.layout=html.Div(
    dbc.Container(
        dbc.Tabs(
            [
                dbc.Tab(
                    [
                        html.Br(),
                        html.P('这是选项卡1'),
                    ],
                    label="选项卡1",
                    tab_style={'background-color':'lightgrey'}#设置表格样式
                ),
                dbc.Tab(
                    [
                        html.Br(),
                        html.P('这是选项卡2'),
                    ],
                    label="选项卡2",
                    label_style={'color':'red'}#设置标签样式
                ),
                dbc.Tab(
                    [
                        html.Br(),
                        html.P('这是选项卡3'),
                    ],
                    label="选项卡3",
                    tab_style={'margin-left':'auto'},
                    active_label_style={'color':'green'}
                ),

            ]
        ),
        style={"margin-top":"100px"}
    )
)

if __name__=="__main__":
    app.run_server(debug=True)