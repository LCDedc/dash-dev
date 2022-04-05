# 配合flask进行下载,开发一个简版的百度网盘
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_uploader as du
from flask import send_from_directory
import os
from dash.dependencies import Output, Input, State
import time

app = dash.Dash(__name__, suppress_callback_exceptions=True)

du.configure_upload(app, folder='NetDisk', use_upload_id=False)

app.layout = html.Div(
    dbc.Container(
        [
            html.H3('简易的个人网盘应用'),
            html.Hr(),
            html.P('文件上传区'),
            du.Upload(id='upload',
                      text='点击或拖动文件到此进行上传',
                      text_completed='已完成文件上传',
                      max_files=1000),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Button('删除选中的文件', id='delete-btn', outline=True),
                    dbc.Button('打包下载选中的文件', id='download-btn', outline=True)
                ]
            ),
            html.Hr(),
            dbc.Spinner(
                dbc.Checklist(
                    id='file-list-check'
                )
            ),
            html.A(id='download-url', target='_blank')
        ]
    )
)


@app.server.route('/download/<file>')
def download(file):
    return send_from_directory('NetDisk', file)


@app.callback(  # 弄清楚output的第二个参数有哪些选择
    [
        Output('file-list-check', 'options'),#所有的文件清单
        Output('download-url', 'children'),#下载文件的值
        Output('download-url', 'href')#下载文件的链接
    ],
    [
        Input('upload', 'isCompleted'),
        Input('delete-btn', 'n_clicks'),
        Input('download-btn', 'n_clicks')
    ],
    State('file-list-check', 'value')
)
def render_file_list(isCompleted, delete_n_clicks, downlaod_n_clicks, check_value):
    # 获取上下文信息
    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id'] == 'delete-btn.n_clicks':
        for file in check_value:
            try:
                os.remove(os.path.join('NetDisk', file))
            except FileNotFoundError:
                pass
    if ctx.triggered[0]['prop_id'] == 'download-btn.n_clicks':
        import zipfile

        with zipfile.ZipFile('NetDisk/打包下载.zip', 'w') as zipobj:
            for file in check_value:
                try:
                    zipobj.write(os.path.join('NetDisk', file))
                except FileNotFoundError:
                    pass
        return [
                   {'label': file, 'value': file}
                   for file in os.listdir('NetDisk')
                   if file != '打包下载.zip'
               ], '打包下载链接', '/download/打包下载.zip'
    time.sleep(2)

    return [
               {'label': file, 'value': file}
               for file in os.listdir('NetDisk')
               if file != '打包下载.zip'
           ], '', ''


if __name__ == '__main__':
    app.run_server(debug=True)
