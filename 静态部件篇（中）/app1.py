import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
#构建一张完整的表格是需要六个部件，Ttable,Thead，Tbody，Tr,Th,Td

app=dash.Dash(__name__)

app.layout=html.Div(
    dbc.Container(
        dbc.Table(
            [
                html.Thead(
                    html.Tr(
                        [
                            html.Th("第一列"),#Th有加粗的作用
                            html.Th("第二列"),
                            html.Th("第三列"),
                            html.Th("第四列")
                        ]
                    )
                ),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Td("一行一列"),
                                html.Td("合并列",colSpan=2,style={"text-align":"center"}),
                                html.Td("一行三列")
                            ]
                        ),
                        html.Tr(
                            [
                                html.Td("二行一列"),
                                html.Td("合并行",rowSpan=2,style={"text-align":"center"}),
                                html.Td("二行三列")
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th("三行一列"),
                                html.Th("三行二列"),
                                html.Th("三行三列"),
                            ]
                        )
                    ]
                )
            ],
            dark=False,#背景设置为黑色
            borderless=False,#内框线不要
            striped=True,#相邻行不要同色
            hover=True,#鼠标悬浮会有相应的效果
            bordered=True
        ),
        style={
             "margin-top":"50px"
        },
    )
)

if __name__=='__main__':
    app.run_server(debug=True)