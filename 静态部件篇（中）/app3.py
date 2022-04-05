#直接使用数据框生成网页表格，缺点是自由度比较低
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

fake_df=pd.DataFrame(np.random.rand(1000).reshape(200,5))
fake_df.rename(lambda s:f'字段{s}',axis=1,inplace=True)

app=dash.Dash(__name__)

app.layout=html.Div(
    dbc.Container(
        dbc.Table.from_dataframe(fake_df,striped=True),
        style={
            'margin-top':'50px'
        }
    )
)

if __name__=='__main__':
    app.run_server(debug=True)