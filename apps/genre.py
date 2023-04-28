import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app
import dash_bootstrap_components as dbc

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

dfv = pd.read_csv(DATA_PATH.joinpath("completely_cleaned_anime.csv")) 
num_list = ['duration', 'votes', 'user_review', 'Episodes']
v=['genre1','Type']


layout = html.Div([
    html.H1('Anime Genre', style={"textAlign": "center"}),

    html.Div([
        html.Div(dcc.Dropdown(
            id='num-dropdown', value='Strategy', clearable=False,
            options=[{'label': x, 'value': x} for x in v]
        ), className='six columns'),

        html.Div(dcc.Dropdown(
            id='genre-dropdown', value='EU Sales', clearable=False,
            persistence=True, persistence_type='memory',
            options=[{'label': x, 'value': x} for x in num_list]
        ), className='six columns'),
    ], className='row'),

    dcc.Graph(id='my-bar', figure={}),
    
    dbc.Container([
                    dbc.Row([
                       
                        dbc.Col(html.H6("Below are some insites for genre : :", className="text-center")
                                , className="mb-5 mt-5")
                    ]),
                   
                    
                    dbc.Row([

                        dbc.Col(html.H5(children=html.P(['-We can see that votes and user reviews follow a similar trend', html.Br(),' -Even though the genre crime has a lesser episodes and duration it has more votes and user review than adventure', html.Br(),'-This is due to the popular anime Death note', html.Br(),'-The least poplar genre by imdb were horror short sports family scifi and fantasy ', html.Br(),'-The highest episodes for an anime was doremon with  2877 episodes ', html.Br(),'-IMDB does seem to have a trend/bias where it does select more action genre in its list ']))
                                        , className="mb-5")
                        
                        ]),
                    dbc.Row([
                       
                        dbc.Col(html.H6("Below are some insites for Type : ", className="text-center")
                                , className="mb-5 mt-5")
                    ]),
                    dbc.Row([

                        dbc.Col(html.H5(children=html.P([' -TV14 which means its not sutible for kids under 14 it the most popular type for an anime ', html.Br(),'-TV MA has the second highest votes, user_reviews and duration which is suprisong as its 18+', html.Br(),'-They do make more episodes for TV PG and TV 14 which means theres a huge watchtime for these animes for kids between 7-14']))
                                        , className="mb-5")
                        
                        ]),
                    
                    ])
])


@app.callback(
    Output(component_id='my-bar', component_property='figure'),
    [Input(component_id='num-dropdown', component_property='value'),
     Input(component_id='genre-dropdown', component_property='value')]
)
def display_value(genre_chosen, num_chosen):
    fig = px.bar(dfv, x=genre_chosen, y=num_chosen, color=num_chosen,hover_data=['name','ratings','Episodes'])
    
    
    return fig


