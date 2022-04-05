# 开发web能够查询英雄联盟的英雄信息
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import requests

# 爬取英雄联盟官方信息

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/98.0.4758.109 Mobile Safari/537.36'}
target = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'

hero_list = requests.get(target, headers=headers).json()


def query_hero_info(hero_id):
    hero_info = requests.get('https://game.gtimg.cn/images/lol/act/img/js/hero/%s.js' % hero_id,
                             headers=headers).json()
    return hero_info


# 这里使用external_scripts导入最后轮播图所需要的js依赖
# 这里用external_scripts导入最后的轮播图所需的js依赖
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=False,
    external_scripts=["https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js",
                      "https://cdn.staticfile.org/popper.js/1.15.0/umd/popper.min.js",
                      "https://cdn.staticfile.org/twitter-bootstrap/4.3.1/js/bootstrap.min.js"]
)
app.layout = html.Div(
    dbc.Container(
        [
            html.H1("LOL-全英雄查看器（免费版）"),
            html.H5('开发者：黎长读   时间：2022年2月26日下午17点：20'),
            html.Br(),
            html.Br(),
            dbc.Form(
                [
                    # 英雄选择控件
                    dbc.FormGroup(
                        [
                            dbc.Label('选择英雄名称：'),
                            dcc.Dropdown(id='hero_list',
                                         options=[
                                             {'label': item['name'], 'value': item['heroId']}
                                             for item in hero_list['hero']
                                         ])
                        ]
                    ),

                    # 查看内容选择空间
                    dbc.FormGroup(
                        [
                            dbc.Label('选择要查看的内容：', html_for='hero_attributes'),
                            dcc.Dropdown(id='hero_attributes',
                                         multi=True,
                                         options=[
                                             {'label': item, 'value': item}
                                             for item in ['基础属性', '技能介绍', '皮肤一览']
                                         ])
                        ]
                    ),

                    # 提交查询按钮
                    dbc.FormGroup(
                        [
                            dbc.Button('查　询', id='query')
                        ]
                    )
                ]
            ),

            # 将渲染的内容包裹在Spinner中实现加载动画
            dbc.Spinner(
                dbc.Tabs(
                    id='hero_attributes_list'
                )
            )
        ],
        style={
            'margin-top': '30px',
            'max-width': '800px'
        }
    )
)


@app.callback(
    Output('hero_attributes_list', 'children'),
    Input('query', 'n_clicks'),
    [State('hero_list', 'value'),
     State('hero_attributes', 'value')]
)
def render_content(n_clicks, hero_id, hero_attributes):
    '''根据用户部件输入结果，进行相应的查询结果的渲染'''
    if n_clicks:
        if hero_id and hero_attributes:
            '''获取英雄的全部信息'''
            hero_info = query_hero_info(hero_id)

            # 初始化返回接轨
            tabs = []
            if '基础属性' in hero_attributes:
                tabs.append(
                    dbc.Tab(
                        [
                            html.H2(hero_info['hero']['name']),
                            html.H5(hero_info['hero']['title']),
                            html.H6(hero_info['hero']['alias']),
                            html.P(
                                ' '.join(
                                    [
                                        '基础生命值' + hero_info['hero']['hp'].split('.')[0],
                                        '基础法力值' + hero_info['hero']['mp'].split('.')[0],
                                        '基础移速' + hero_info['hero']['movespeed'].split('.')[0],
                                        '基础攻击力' + hero_info['hero']['attackdamage'].split('.')[0]
                                    ]
                                )
                            ),
                            html.Img(
                                src=hero_info['skins'][0]['mainImg'],
                                style={'width': '100px'}
                            )
                        ],
                        label='基础属性'
                    )
                )
            if '技能介绍' in hero_attributes:
                '''#自定义排序，方便正常的排序'''
                CUSTOM_ORDER = {'passive': 0, 'q': 1, 'w': 2, 'e': 3, 'r': 4}
                skills = sorted(hero_info['spells'], key=lambda item: CUSTOM_ORDER[item['spellKey']])
                tabs.append(
                    dbc.Tab(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src=skill['abilityIconPath']), width=1),
                                    dbc.Col([html.P(skill['spellKey'].upper().replace('PASSIVE', '被动') +
                                                    '技能：' + skill['name'], style={'font-weight': 'bold'}),
                                             html.P(skill['description'])])
                                ],
                                justify='start'
                            )
                            for skill in skills
                        ],
                        label='技能介绍'
                    )
                )
            if '皮肤一览' in hero_attributes:
                hero_info['skins'] = [skin for skin in hero_info['skins'] if skin['mainImg'] != ""]
                print(hero_info['skins'][-1])

                tabs.append(
                    dbc.Tab(
                        [
                            html.Div(
                                [
                                    html.Ul(
                                        [
                                            html.Li(**{
                                                'data-target': '#demo',
                                                'data-slide-to': '0',
                                                'className': 'active'
                                            })
                                        ] +
                                        [
                                            html.Li(**{
                                                'data-target': '#demo',
                                                'data-slide-to': str(i)
                                            })
                                            for i in range(1, hero_info['skins'].__len__())
                                        ],
                                        className='carousel-indicators'
                                    ),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Img(
                                                        src=hero_info['skins'][0]['mainImg']
                                                    ),
                                                    html.Div(
                                                        html.H2(hero_info['skins'][0]['name']),
                                                        className='carousel-caption'
                                                    )
                                                ],
                                                className='carousel-item active'
                                            )
                                        ] + [
                                            html.Div(
                                                [
                                                    html.Img(
                                                        src=skin['mainImg']
                                                    ),
                                                    html.Div(
                                                        html.H2(skin['name']),
                                                        className='carousel-caption'
                                                    )
                                                ],
                                                className='carousel-item'
                                            )
                                            for skin in hero_info['skins'][1:]
                                        ],
                                        className='carousel-inner'
                                    ),

                                    html.A(
                                        html.Span(className='carousel-control-next-icon'),
                                        className='carousel-control-next',
                                        href='#demo',
                                        **{'data-slide': 'next'}
                                    )
                                ],
                                id='demo',
                                className='carousel slide',
                                **{'data-ride': 'carousel'}
                            )
                        ],
                        label='皮肤一览'
                    )
                )
            return tabs
    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)
