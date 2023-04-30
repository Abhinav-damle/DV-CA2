import dash
from dash import html
import dash_bootstrap_components as dbc



from app import app


layout = html.Div([
    dbc.Container([
        dbc.Row([
   
            dbc.Col(html.H1("Welcome to Anime Hub ", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H3(children='What is anime?' 
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='Anime is hand-drawn and computer-generated animation originating from Japan. Outside of Japan and in English, anime refers specifically to animation produced in Japan ')
                    , className="mb-5")
        ]),
        
        dbc.Row([
            dbc.Col(html.H3(children='Understanding the dataset')
                    , className="mb-5")
        ]),
        
        dbc.Row([
            dbc.Col(html.H5(children='The dataset is scraped from imdbs most popular anime')
                    , className="mb-5")
        ]),
                dbc.Row([
                    dbc.Col(html.Img(src=app.get_asset_url('dataset.png'), 
                    style={'height':'70%', 'width':'50%'}))
                ]),
        dbc.Row([
            dbc.Col(html.H5(children='The columns are as follows:')
                    , className="mb-5")
        ]),
        
        dbc.Row([

            dbc.Col(html.H5(children=html.P(['name:name of the anime', html.Br(), 'duration:Lenght of each episode or movie', html.Br(),'ratings:imdb rating of the anime', html.Br(),'votes:votes recived on imdb ', html.Br(),'user review:the number of user review on imdb', html.Br(),'Type:The type of anime it was released as', html.Br(),'Episodes:The number of episodes for the anime', html.Br(),'start_year:The start year of the anime', html.Br(),'end_year: The year the anime is ended or scheducled to end', html.Br(),'genre1: The main genre of the anime ', html.Br(),'genre2: The subgenre of the anime ', html.Br(),'rank:The rank that was given by IMDB']))
                            , className="mb-5")
            
            ]),


        dbc.Row([
  
            dbc.Col(dbc.Card(children=[html.H3(children='Go to the code',
                                               className="text-center"),
                                       dbc.Button("Github Data",
                                                  href="https://github.com/Abhinav-damle/DV-CA2",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Access  the dataset',
                                               className="text-center"),
                                       dbc.Button("Gihub",
                                                  href="https://github.com/Abhinav-damle/dataset.git",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-4"),

        ], className="mb-5"),
        dbc.Row([
            dbc.Col(html.Img(src=app.get_asset_url('banner.jfif'), 
            style={'height':'30%', 'width':'100%'}))
        ]),
        html.A("Anime for lifeee",
               href="https://www.imdb.com/list/ls058654847/?st_dt=&mode=detail&page=1&sort=list_order,asc")

    ])

])

