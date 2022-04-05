import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import pandas as pd
from sqlalchemy import create_engine
import pymysql

postgres_url = 'mysql+pymysql://root:123456@39.105.11.250/analysis'
engine = create_engine(postgres_url)

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Button('更新数据库信息', id='refresh-db', style={'width': '100%'}), width=2),
                    dbc.Col(dcc.Dropdown(id='db-table-names', placeholder='选择库中数据表', style={'width': '100%'}),
                            width=4),
                    dbc.Col(dbc.Button('查询', id='query', style={'width': '100%'}), width=1)
                ]
            ),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(
                        id='query-result'  # 查询结果
                    )
                ]
            )
        ],
        style={
            'margin-top': '50px'  # 设置顶部留白区域高度
        }
    )
)


@app.callback(
    Output('db-table-names', 'options'),  # 输出表格名字
    Input('refresh-db', 'n_clicks'),  # 点击刷新按钮
    prevent_initial_call=True
)
def refresh_table_names(n_clicks):  # 函数是查询
    table_names = pd.read_sql_query("select table_name from information_schema.tables where table_schema='analysis'",
                                    con=engine)
    return [{'label': name, 'value': name} for name in table_names['TABLE_NAME']]


@app.callback(
    Output('query-result', 'children'),  # 输出查询结果
    Input('query', 'n_clicks'),  # 输出点击查询按钮
    State('db-table-names', 'value'),  # 下拉框的显示
    prevent_initial_call=True  # 初始不要默认查询
)
def query_data_records(n_clicks, value):
    if value:
        # 提取目标表格并查询其最多前500行记录
        query_result = pd.read_sql_query(f'select * from {value} limit 500', con=engine)

        return html.Div(dbc.Table.from_dataframe(query_result, striped=True),
                        style={'height': '600px', 'overflow': 'auto'})
    else:
        return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)
