import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_uploader as du

app = dash.Dash(__name__)
# 配置上传文件夹
du.configure_upload(app, folder='temp')  # 会生成temp文件夹用来保存上传的文件

app.layout = html.Div(
    dbc.Container(
        [
            du.Upload()
        ]
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)
