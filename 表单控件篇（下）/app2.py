#fromfeedback验证输入内容是否满足
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output

app=dash.Dash(__name__)

app.layout=html.Div(
    dbc.Container(
        [
            dbc.Form(
                [
                    dbc.FormGroup(
                        [
                            dbc.Label("账号密码",html_for='password'),
                            dbc.Input(
                                id='password',
                                placeholder='请输入密码',
                                autoComplete='off'
                            ),
                            dbc.FormText(
                                "密码至少包含大写字母、小写字母和数字！",color='secondary'
                            ),
                            dbc.FormFeedback(
                                "密码格式满足要求！",valid=True
                            ),
                            dbc.FormFeedback(
                                "密码格式不满足要求！",valid=False
                            ),
                        ]
                    )
                ]
            )
        ],
        style={
            "margin-top":'200px',
            'max-width':"400px"
        }
    )
)

@app.callback(
    [
        Output('password','valid'),
        Output('password','invalid')
    ],
    Input('password','value')
)
def check_password_format(value):
    import re

    if value:
        if all([#检查密码是否符合要求
                re.search('[a-z]',value),
                re.search('[A-Z]',value),
                re.search('[0-9]',value),
                value.__len__()!=0
        ]):
            return True,False
        else:
            return False,True

    return dash.no_update

if __name__=='__main__':
    app.run_server(debug=True)