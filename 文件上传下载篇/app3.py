# 每个上传的文件保持唯一性
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_uploader as du

app = dash.Dash(__name__)

du.configure_upload(app, folder="temp")  # 配置文件夹


def render_random_id_uploader():#设置格式
    return du.Upload(id='uploader',
                     text='点击或者拖动文件到此进行上传',
                     text_completed="已完成文件上传",
                     cancel_button=True,
                     pause_button=True,
                     filetypes=['md', 'mp4', 'pdf'],
                     default_style={
                         'background-color': "#fafafa",
                         "font-weight": 'bold'
                     },
                     upload_id=uuid.uuid1()
                     )


def render_layout():#设置app
    return html.Div(
        dbc.Container(
            render_random_id_uploader()
        )
    )


app.layout = render_layout

if __name__ == '__main__':
    app.run_server(debug=True)
