import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app
import dash_bootstrap_components as dbc


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()


dfv = pd.read_csv(DATA_PATH.joinpath("completely_cleaned_anime2.csv")) 
num_list = ['duration', 'ratings', 'user_review', 'Episodes']
v=['top10-rank','top20-rank','top100-rank']
year=dfv.sort_values('start_year', ascending=True)
m=list(year.start_year.unique())
l=list(year.start_year.value_counts(ascending=True))
new_df=dfv[dfv.start_year<2000]
num= ['duration', 'ratings', 'user_review', 'Episodes']
fig2=px.line(x=m,y=l,title="Yearly releases of animes").update_layout(xaxis_title="Year", yaxis_title="anime_count")
layout = html.Div([
    
    
    html.Div(
    [
        html.H4("Different genres with a selectable hover mode"),
        html.P("Select hovermode:"),
        dcc.RadioItems(
            id="hovermode",
            inline=True,
            options=["genre1", "genre2", "Total genre"],
            value="closest",
        ),
        dcc.Graph(id="graph"),    
        dbc.Container([
                dbc.Row([

                    dbc.Col(html.H6(children=html.P(['  ', html.Br(),' ', html.Br(),'-Looking at all 3 we can tell that animes have a different count for genre and subgenre', html.Br(), '-From the main genre we can tell that Action has the most animes followed by comedy ', html.Br(),'-But in the subgenre its drama that has the most animes with action not even making it in the list ', html.Br(),'-Hence when we add these genres together it doesnt make any difference in the top order but makes a difference in the bottom order ']))
                                    , className="mb-5")
                    
                    ]),
                ])
    ]
),
    html.Div([
    html.H4('Scatterplot between votes and user_reviews'),
    dcc.Graph(id="scatter-plot"),
    html.P("Filter with ratings"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=9.8, step=0.5,
        marks={0: '0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9', 9.8: '9.8'},
        value=[0, 9.8]
    ),        dbc.Container([
                   dbc.Row([

                       dbc.Col(html.H6(children=html.P(['  ', html.Br(),' ', html.Br(),'-There seems to be a linear relationship btween the two', html.Br(),'-There are no anime below a rating of 5', html.Br(),'-Most of the anime are between the ratings 6 and 8']))
                                       , className="mb-5")
                       
                       ]),])
]),
    html.Div([
      
       html.Div([
            html.H3('Yearly releases of animes'),
            dcc.Graph(id='g3', figure=px.line(x=m,y=l).update_layout(xaxis_title="Year", yaxis_title="anime_count"))
        ], className="six columns"),
       dbc.Container([
                      dbc.Row([

                          dbc.Col(html.H6(children=html.P(['  ', html.Br(),' ', html.Br(),'          -Anime rose in the early 2000', html.Br(),'          -We can have a better look at this from the below graph ']))
                                          , className="mb-5")
                          
                          ]),])
    ], className="row"),
  
    html.Div([
      
       html.Div([
            html.H3('Anime released on/beofre 2000'),
        ], className="six columns"),
    ], className="row"),
    
    html.Div([
        html.Div(dcc.Dropdown(
            id='numdropdown', value='Strateg', clearable=False,
            options=[{'label': x, 'value': x} for x in num]
        ), className='six columns'),

    ], className='row'),

    dcc.Graph(id='mybar', figure={}),
    
    dbc.Row([
 
        dbc.Col(html.H6(children=html.P(['  ', html.Br(),' ', html.Br(),'          -As seen above animes like one piece , shen seiki and pokemon boasted the views ', html.Br(),'          -and animes like doremon came up with more episodes by boasting the watchtime ']))
                        , className="mb-5")
    ]),
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

@app.callback(
    Output("graph", "figure"),
    Input("hovermode", "value"),
)


def display_value(x):
    s=dfv.genre1.value_counts()
    genre1= pd.DataFrame({'genre1':s.index, 'Count':s.values})
    s=dfv.genre2.value_counts().head(11)
    genre2= pd.DataFrame({'genre2':s.index, 'Count':s.values})

            
        
     
    if x=='genre1':
        genre1=genre1.sort_values('Count', ascending=False)
        fig = px.bar(genre1,x='genre1', y='Count', 
              title = 'votes of top10 anime')
        return fig

    elif x=='genre2':
         genre2=genre2.sort_values('Count', ascending=False)
         fig = px.bar(genre2,x='genre2', y='Count', 
               title = 'votes of top10 anime')
         return fig       
        
    else:
        for i in range(0,11):
            for j in range(0,11):
                if genre1.genre1[i]==genre2.genre2[j]:
                    genre1.Count[i]=genre1.Count[i]+genre2.Count[j]
        genre1=genre1.sort_values('Count', ascending=False)
        fig = px.bar(genre1,x='genre1', y='Count', 
               title = 'votes of top10 anime')
        return fig   

@app.callback(
    Output("scatter-plot", "figure"), 
    Input("range-slider", "value"))
def update_bar_chart(slider_range):

    low, high = slider_range
    mask = (dfv['ratings'] > low) & (dfv['ratings'] < high)
    fig = px.scatter(
        dfv[mask], x="votes", y="user_review", 
        hover_data=['name'],trendline="ols")
    return fig


@app.callback(
    Output(component_id='mybar', component_property='figure'),
    Input(component_id='numdropdown', component_property='value'))

def x( num_chosen):
    fig = px.bar(new_df, x='genre1', y=num_chosen, color=num_chosen,hover_data=['name','ratings','Episodes','start_year'])
    return fig