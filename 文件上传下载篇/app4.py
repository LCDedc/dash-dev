#配合回调
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_uploader as du
from dash.dependencies import Input,Output,State

app= dash.Dash(__name__)

#配置上传文件夹
du.configure_upload(app,folder="temp")

app.layout=html.Div(
    dbc.Container(
        [
            du.Upload(id='uploader'),
            html.H5('上传中或还未上传文件！',id='uploader_status')
        ]
    )
)

@app.callback(
    Output('uploader_status','children'),
    Input('uploader','isCompleted'),
    State('uploader','fileNames')
)

def show_upload_status(isCompleted,fileName):
    if isCompleted:
        return '已完成上传：'+fileName[0]
    return dash.no_update

if __name__=='__main__':
    app.run_server(debug=True)
