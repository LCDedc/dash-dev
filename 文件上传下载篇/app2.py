# 制作复杂的文件上传和下载

import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_uploader as du

app = dash.Dash(__name__)

du.configure_upload(app, folder="temp")  # 配置文件夹

app.layout = html.Div(
    dbc.Container(
        [
            du.Upload(id='uploader',
                      text='点击或者拖动文件到此进行上传',
                      text_completed="已完成文件上传",
                      cancel_button=True,
                      pause_button=True,
                      filetypes=['md', 'mp4', 'pdf'],
                      default_style={
                          'background-color': "#fafafa",
                          "font-weight": 'bold'
                      },
                      upload_id="我的上传"
                      )
        ]
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)
