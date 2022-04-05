#利用dash_html_components中的Blockquote()，我们可以直接传入字符串，或嵌套其他元素，从而构造出块引用，
# 就像markdown中的>所包含渲染的内容那样，参考下面的例子
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        html.Blockquote(
            html.P('这是一段由块引用包裹的文字内容' * 10),
            style={
                'background-color': 'rgba(211, 211, 211, 0.25)',
                'text-indent': '3rem'
            }
        )
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)