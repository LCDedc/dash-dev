#实现悬浮提示框
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app=dash.Dash(__name__)

app.layout=html.Div(
    dbc.Container(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            html.P(
                [
                    "在",html.A('Dash',
                               href='https://dash.plotly.com/',
                               id="dash"),
                    '中，我们可以使用',
                    html.A('dash_bootstrap_components',
                           href='https://github.com/facultyai/dash-bootstrap-components',
                           id='dash_bootstrap_components'),
                    '来快速完成基于网格系统的页面布局',
                    dbc.Tooltip('Dash是一整套基于python的web应用快速搭建方案。',target="dash",delay={'show':0,'hide':900}),
                    #提示框绑定id
                    dbc.Tooltip('dash_bootstrap_components是Dash第三方拓展中对bootstrap诸多工具的迁移。',
                                target='dash_bootstrap_components')
                ]
            )
        ]
    )
)

if __name__=='__main__':
    app.run_server(debug=True)
