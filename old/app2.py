import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table

import pandas as pd
import plotly.graph_objects as go

c0='rgba(255,64,0,0.4)';
c1='rgba(0,64,255,0.4)';

c2='rgba(200,32,51,0.8)';
c3='rgba(153,51,0,0.8)';
c4='rgba(255,100,100,0.8)';
c5='rgba(255,155,0,0.8)';
c6='rgba(255,0,0,0.8)';

c7='rgba(0,96,255,0.8)';
c8='rgba(100,100,255,0.8)';
c9='rgba(153,0,205,0.8)';
c10='rgba(100,100,155,0.8)';

c11='rgba(255,128,255,0.95)';
c12='rgba(128,255,128,0.95)';
c13='rgba(128,255,255,0.95)';

c14='rgba(255,200,100,0.6)';
c15='rgba(255,128,90,0.6)';
c16='rgba(128,128,20,0.6)';
c17='rgba(0,255,128,0.6)';

c18='rgba(0,0,0,.4)';

c19='rgba(0,128,255,0.2)';

c20='rgba(255,128,255,0.85)';
c21='rgba(255,128,255,0.85)';
c22='rgba(255,128,255,0.85)';

c23='rgba(0,160,128,0.85)';
c24='rgba(0,160,128,0.85)';
c25='rgba(0,160,128,0.85)';
c26='rgba(0,160,128,0.85)';

c27='rgba(128,255,255,0.85)';
c28='rgba(128,255,255,0.85)';

df = pd.read_csv('datatable.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.title='Neuro in HE: SLR'

app.layout = html.Div([
    html.Div([
        html.H1(children='The Use of Neurophysiological Measurements and Instruments in Higher Education: A Systematic Literature Review'),
        ],
             style={
                 'width':'100%',
                 'display': 'block',
                 'color': 'rgb(255,255,255)',
                 'backgroundColor': 'rgb(81,36,122)',
                 'borderBottom': 'grey solid','borderTop': 'grey solid',}
            ),
    html.Div([
        html.H3(children='Filter by',),
        ],
             ),
    html.Div([
        html.Div([
            html.H5(children='Year:',),
            dcc.Dropdown(
                            id='year-select',
                            options=[
                                        {'label': 'Total', 'value': 2019},
                                        {'label': '2018', 'value': 2018},
                                        {'label': '2017', 'value': 2017},
                                        {'label': '2016', 'value': 2016},
                                        {'label': '2015', 'value': 2015},
                                        {'label': '2014', 'value': 2014}
                                    ], 
                           value=[2019],
                            multi=True,
                        ),
            ]
                 ),
        html.Div([
            html.H5(children='Measure:',),
            dcc.Dropdown(
                id='measure-select',
                options=[
                                                {'label': 'Total', 'value': 'Total'},
                                                {'label': 'Facial', 'value': 'Facial'},
                                                {'label': 'Eye', 'value': 'Eye'},
                                                {'label': 'Heart', 'value': 'Heart'},
                                                {'label': 'Skin', 'value': 'Skin'},
                                                {'label': 'Blood', 'value': 'Blood'},
                                         
                                                {'label': 'EEG', 'value': 'EEG'},
                                                {'label': 'fMRI', 'value': 'fMRI'},
                                                {'label': 'NIRS', 'value': 'NIRS'},
                                                {'label': 'fNIR', 'value': 'fNIR'}
                        ],
                value=['Total'],
                multi=True,
                ),
            ],
                 ),
        html.Div([
            html.H5(children='Construct:',),
            dcc.Dropdown(
                                    id='construct-select',
                                    options=[
                                
                      
                                                {'label': 'Total', 'value': 'Total'},
                                                {'label': 'Attention', 'value': 'Attention'},
                                                {'label': 'Cognitive load', 'value': 'Cognitive load'},
                                                {'label': 'Skill', 'value': 'Skill'},
                                                
                                                {'label': 'Attitudes and beliefs', 'value': 'Attitudes and beliefs'},
                                                {'label': 'Social and emotional qualities', 'value': 'Social and emotional qualities'},                                 
                                                {'label': 'Habits and processes', 'value': 'Habits and processes'},
                                                {'label': 'Personality traits', 'value': 'Personality traits'},
                                                
                                                {'label': 'Knowledge about cognition', 'value': 'Knowledge about cognition'},
                                                {'label': 'Self-regulation of cognition', 'value': 'Self-regulation of cognition'}
                                            ], 
                                   value=['Total'],
                                     multi=True,
                        ),
            ],
                 ),
        ],
             style={'display': 'inline','width':'30%',
                                            'float':'left',
                                            'backgroundColor': 'rgb(250, 250, 250)',
                                            'padding': '10px 5px'
                    },
             ),
    html.Div([
        dcc.Graph(id='graph-with-select'),
        ],
             style={'width':'50%','float':'right','display': 'inline-block'}
             ),


html.Div([
           html.H3(id='text-title'),
           ],style={
                 'width':'100%',
                 'display': 'inline-block',
                 'borderBottom': 'grey solid','borderTop': 'grey solid',}
             ),
html.Div([
    
    dcc.Graph(id='graph-with-participant'),
    ],style={
                 'width':'100%',
                 'display': 'inline-block',
                 'borderBottom': 'grey solid','borderTop': 'grey solid',}
             ),
 
html.Div([
    dcc.Graph(id='graph-with-sankey'),
    ],
             style={
                 'width':'100%',
                 'display': 'inline-block',
                 'borderBottom': 'grey solid','borderTop': 'grey solid',}
             ),
html.Div([
       html.H3(children='Summary of the selected studies',), 
    dash_table.DataTable(
        id='table',
        	
        			 		 

        columns=[
                  {"name":'Title', "id":'Title'},  
                  {"name":'Author/s', "id":'Author/s'},  
                  {"name":'Year', "id":'Pub Year'},  
                  {"name":'Q1.1. Neuro Measurement Instruments', "id":'Q1.1. Neuro Measurement Instruments'},
                  {"name":'Q1.2. Non-neuro Measurements', "id":'Q1.2. Non-neuro Measurements'},
                  
                  {"name":'Q2.1. Study Setting', "id":'Q2.1. Study Setting'},  
                  {"name":'Q2.2. Experimental Design', "id":'Q2.2. Experimental Designs'},  
                  {"name":'Q2.3. participants - recruitments', "id":'Q2.3. participants - recruitments'},  
                  {"name":'Q2.4. Ethical considerations', "id":'Q2.4. Ethical considerations'},  
                  {"name":'Q2.5. Intrusiveness - devices', "id":'Q2.5. Intrusiveness - devices'},  
                  {"name":'Q2.6. Number of participants', "id":'Total '},  
                  {"name":'Q2.7. Reproducibility', "id":'Q2.7. Reproducibility'},  
                  {"name":'Q3.1. Psychological constructs', "id":'Q3.1. Psychological constructs'},  
                  {"name":'Q3.3. Reported outcomes (Purposes)', "id":'Q3.3. Reported outcomes (Purposes)'},  

                ],
        style_table={'overflowX': 'scroll'},
        style_data={
                    
                    'border': ' solid blue',
                    
                    },
        fixed_rows={ 'headers': True, 'data': 0 },
        style_header={ 'border': ' solid black' },
       style_cell={'whiteSpace': 'normal',
                   'textAlign': 'left',
                   'minWidth': '0px', 'maxWidth': '180px',
                   'height': 'auto'},

        style_cell_conditional=[
        {'if': {'column_id': 'Total '},
         'width': '120px'},
        {'if': {'column_id': 'Title'},
         'width': '300px'},
       {'if': {'column_id': 'Total '},
         'width': '85px'},
       {'if': {'column_id': 'Q1.1. Neuro Measurement Instruments'},
         'width': '70px'},
       {'if': {'column_id': 'Q1.2. Non-neuro Measurements'},
         'width': '40px'},
       {'if': {'column_id': 'Q2.2.Q2.2. Experimental Designs'},
         'width': '20px'},

    ]
           ) 
    ],

             ),
    ],
                      )






##########################################################SANKEY##################################################################################

@app.callback(
    Output('graph-with-sankey', 'figure'),
    [Input('year-select', 'value'),
    Input('measure-select', 'value'),
     Input('construct-select', 'value')])

def update_figure(selected_year,selected_measure,selected_construct):
    skip=0
    skipm=0
    skipc=0
    dff1=df[df['Pub Year'] < 2014]
    dff2=df[df['Pub Year'] < 2014]
    measure=selected_measure
    construct=selected_construct

    for i in selected_year:
        if i == 2019 :
            skip=1
        
    if skip==1 :
        dff = df[df['Pub Year'] < 2019]
        year='all years'
        pm='temp'
    if skip == 0:
        dff = df[df['Pub Year'].isin(selected_year)]
        year=selected_year
        measure=selected_measure
        construct=selected_construct
    for i in selected_measure:
        if i == 'Total' :
            measure='all measures'
            skipm=1
            dff1=dff
        if i == 'Facial' :
            dff1 =dff1.append(dff[dff['Facial'] == 1])            
        if i == 'Eye' :
            dff1 =dff1.append(dff[dff['Eye'] == 1])
        if i == 'Heart' :
            dff1 =dff1.append(dff[dff['Heart'] == 1])
        if i == 'Skin' :
            dff1 =dff1.append(dff[dff['Skin'] > 0])
        if i == 'Blood' :
            dff1 =dff1.append(dff[dff['Blood'] == 1])
        if i == 'EEG' :
            dff1 =dff1.append(dff[dff['EEG'] == 1])
        if i == 'fMRI' :
            dff1 =dff1.append(dff[dff['fMRI'] == 1])
        if i == 'NIRS' :
            dff1 =dff1.append(dff[dff['NIRS'] == 1])
        if i == 'fNIR' :
            dff1 =dff1.append(dff[dff['fNIR'] == 1])
                 
    ##dff=dff1.drop_duplicates('Title')
##    	attention	load	skills	beliefs 	emotions	habits	traits knowledge	regulation
    for i in selected_construct:
        
        if i == 'Total' :
            construct='all constructs'
            skipc=1
            dff2=dff1        
        if i == 'Attention' :
            
            dff2 =dff2.append(dff1[dff1['attention'] == 1])
            
        if i == 'Cognitive load' :
            
            dff2 =dff2.append(dff1[dff1['load'] == 1])
            
        if i == 'Skill' :
            
            dff2 =dff2.append(dff1[dff1['skills'] == 1])
            
        if i == 'Attitudes and beliefs' :
            
            dff2 =dff2.append(dff1[dff1['beliefs'] == 1])
            
        if i == 'Social and emotional qualities' :
            dff2 =dff2.append(dff1[dff1['emotions'] == 1])
        if i == 'Habits and processes' :
            dff2 =dff2.append(dff1[dff1['habits'] == 1])
        if i == 'Personality traits' :
            dff2 =dff2.append(dff1[dff1['traits'] == 1])
        if i == 'Knowledge about cognition' :
            dff2 =dff2.append(dff1[dff1['knowledge'] == 1])
        if i == 'Self-regulation of cognition' :
            dff2 =dff2.append(dff1[dff1['regulation'] == 1])

    dff=dff2.drop_duplicates('Title')

### attention	cognitive load	skills
### attitudes and beliefs 	social and emotional qualities	habits and processes	personality traits
### knowledge 	self-regulation
### knowledge 	regulation 	attention	load	skills	beliefs 	emotions	habits	traits
        ##int(dff.groupby('attention')['EEG'].count())

        
    dff_attention=dff[dff['attention'] > 0]
    dff_load=dff[dff['load'] > 0]
    dff_skills=dff[dff['skills'] > 0]

    dff_beliefs=dff[dff['beliefs'] > 0]
    dff_emotions=dff[dff['emotions'] > 0]
    dff_habits=dff[dff['habits'] > 0]
    dff_traits=dff[dff['traits'] > 0]


    dff_knowledge=dff[dff['knowledge'] > 0]
    dff_regulation=dff[dff['regulation'] > 0]
### Cognitive	Non-Cognitive	Meta-Cognitive

    dffc=dff[dff['Cognitive'] > 0]
    dffn=dff[dff['Non-Cognitive'] > 0]
    dffm=dff[dff['Meta-Cognitive'] > 0]

    
    traces = []

    traces.append(

            go.Sankey(

    node = dict(
      pad = 5,
      thickness = 10,

      line = dict(color = "black", width = 0.5),
      label = ["ANS", "CNS", #0,1
               "Facial","Eye","Heart","Skin","Blood",#2,3,4,6
               "EEG","fMRI","NIRS","fNIR",#7,8,9,10
               "Cognitive","Non-cognitive","Meta-cognitive",#11,12,13
               "Monitoring States","Performance Estimation","Feedback / Notification","Adaptive System",#14,15,16,17
              # " ","p","f","a",
               "Selected NeuroIS Studies","Outcomes",#18,19
               "Attention","Cognitive load","Skill",#20,21,22
               "Attitudes and beliefs","Social and emotional","Habits and processes","Personality traits",#23,24,25,26
               "Knowledge","Self-regulation "#27,28
              ],

              
      x=  [     .1,.1, #"ANS", "CNS", #0,1
               .2,.2,.2,.2,.2,#"Facial","Eye","Heart","Skin","Blood",#2,3,4,6
               .2,.2,.2,.2,#"EEG","fMRI","NIRS","fNIR",#7,8,9,10
               .8,.78,.78,#"Cognitive","Non-cognitive","Meta-cognitive",#11,12,13
               1,1,1,1,#"Monitoring States","Performance Estimation","Feedback / Notification","Adaptive System",#14,15,16,17
              
               0.01,#"NeuroIS Studies","Outcomes",#18,19
               .7,.7,.7,#"Attention","Cognitive load","Skill",#20,21,22
               .6,.6,.6,.6,#"Attitudes and beliefs","Social and emotional","Habits and processes","Personality traits",#23,24,25,26
               .67,.67,#"Knowledge","Self-regulation "#27,28
              ]
      if ((skip == 1) & (skipm == 1) & (skipc == 1)) else  [],
     y= [      0.1,1,#"ANS", "CNS", #0,1
               0.01,.2,.32,.43,.5,#"Facial","Eye","Heart","Skin","Blood",#2,3,4,6
               .75,.95,1.03,1.1,#"EEG","fMRI","NIRS","fNIR",#7,8,9,10
               .65,0.01,1,#"Cognitive","Non-cognitive","Meta-cognitive",#11,12,13
               0.35,.60,.73,.83,#"Monitoring States","Performance Estimation","Feedback / Notification","Adaptive System",#14,15,16,17
              # " ","p","f","a",
               .5,#"NeuroIS Studies","Outcomes",#18,19
               .5,.85,.7,#"Attention","Cognitive load","Skill",#20,21,22
               .3,0.01,.17,.24,#"Attitudes and beliefs","Social and emotional","Habits and processes","Personality traits",#23,24,25,26
               1,1.1,#"Knowledge","Self-regulation "#27,28
              ]
      if ((skip == 1) & (skipm == 1) & (skipc == 1)) else
      [],
           


                 color='hsv(0,0,0)'

    ),
    link = dict(
                # indices correspond to labels,
      source = [0 , 0, 0,0,0, 1,1,1, 1,
                2,2,2,2,2,2,2,2,2, #facial
                3,3,3,3,3,3,3,3,3,
                4,4,4,4,4,4,4,4,4,
                5,5,5,5,5,5,5,5,5,
                6,6,6,6,6,6,6,6,6,
                7,7,7,7,7,7,7,7,7,
                8,8,8,8,8,8,8,8,8,
                9,9,9,9,9,9,9,9,9,
                10,10,10,10,10,10,10,10,10,

                20,21,22,    #cognitive
                23,24,25,26, #non-cognitve
                27,28,       #meta-cognitive

                11,11,11,11,12,12,12,12,13,13,13,13,
                #14,15,16,17,#Results
                18,  18,],

      target = [2 , 3, 4,5,6, 7,8,9,10,

                20,21,22,23,24,25,26,27,28, #facial
                20,21,22,23,24,25,26,27,28, #Eye
                20,21,22,23,24,25,26,27,28, #Heart
                20,21,22,23,24,25,26,27,28, #Skin
                20,21,22,23,24,25,26,27,28, #Blood
                20,21,22,23,24,25,26,27,28, #EEG
                20,21,22,23,24,25,26,27,28, #fMRI
                20,21,22,23,24,25,26,27,28, #NIRS
                20,21,22,23,24,25,26,27,28, #fNIR

                11,11,11,
                12,12,12,12,
                13,13,

                14,15,16,17,14,15,16,17,14,15,16,17,
                #19,19,19,19,#Results
                0,   1,],

      value =  [
## total:                25,13,11,9,2,38,3,2, 2,

                    int(dff.aggregate(['sum'])['Facial']),int(dff.aggregate(['sum'])['Eye']),
                    int(dff.aggregate(['sum'])['Heart']),int(dff.aggregate(['sum'])['Skin']),
                    int(dff.aggregate(['sum'])['Blood']),int(dff.aggregate(['sum'])['EEG']),
                    int(dff.aggregate(['sum'])['fMRI']),int(dff.aggregate(['sum'])['NIRS']),
                    int(dff.aggregate(['sum'])['fNIR']),
                    
                                    #Constructs mapping
### 3,3,3,1,18,5,0,1,1, #facial int(dff.groupby('attention')['Facial'].count())

               int(dff_attention.aggregate(['sum'])['Facial']),int(dff_load.aggregate(['sum'])['Facial']),int(dff_skills.aggregate(['sum'])['Facial']),
               int(dff_beliefs.aggregate(['sum'])['Facial']),int(dff_emotions.aggregate(['sum'])['Facial']),
               int(dff_habits.aggregate(['sum'])['Facial']),int(dff_traits.aggregate(['sum'])['Facial']),
               int(dff_knowledge.aggregate(['sum'])['Facial']),int(dff_regulation.aggregate(['sum'])['Facial']),
##                    knowledge 	regulation 	attention	load	skills	beliefs 	emotions	habits	traits
                    
##                 int(dff.groupby('attention')['Facial'].count()), int(dff.groupby('load')['Facial'].count()), int(dff.groupby('skills')['Facial'].count()),
##                    int(dff.groupby('beliefs')['Facial'].count()), int(dff.groupby('emotions')['Facial'].count()),
##                    int(dff.groupby('habits')['Facial'].count()), int(dff.groupby('traits')['Facial'].count()),
##                    int(dff.groupby('knowledge')['Facial'].count()), int(dff.groupby('regulation')['Facial'].count()), 

               
###                3,4,4,0,1,0,1,2,2,  #Eye
                    
               int(dff_attention.aggregate(['sum'])['Eye']),int(dff_load.aggregate(['sum'])['Eye']),int(dff_skills.aggregate(['sum'])['Eye']),
               int(dff_beliefs.aggregate(['sum'])['Eye']),int(dff_emotions.aggregate(['sum'])['Eye']),
               int(dff_habits.aggregate(['sum'])['Eye']),int(dff_traits.aggregate(['sum'])['Eye']),
               int(dff_knowledge.aggregate(['sum'])['Eye']),int(dff_regulation.aggregate(['sum'])['Eye']), 

                    
###                4,3,3,0,4,2,0,0,1,  #Heart

               int(dff_attention.aggregate(['sum'])['Heart']),int(dff_load.aggregate(['sum'])['Heart']),int(dff_skills.aggregate(['sum'])['Heart']),
               int(dff_beliefs.aggregate(['sum'])['Heart']),int(dff_emotions.aggregate(['sum'])['Heart']),
               int(dff_habits.aggregate(['sum'])['Heart']),int(dff_traits.aggregate(['sum'])['Heart']),
               int(dff_knowledge.aggregate(['sum'])['Heart']),int(dff_regulation.aggregate(['sum'])['Heart']), 

                    
###                2,2,1,1,5,1,1,0,0,  #Skin

               int(dff_attention.aggregate(['sum'])['Skin']),int(dff_load.aggregate(['sum'])['Skin']),int(dff_skills.aggregate(['sum'])['Skin']),
               int(dff_beliefs.aggregate(['sum'])['Skin']),int(dff_emotions.aggregate(['sum'])['Skin']),
               int(dff_habits.aggregate(['sum'])['Skin']),int(dff_traits.aggregate(['sum'])['Skin']),
               int(dff_knowledge.aggregate(['sum'])['Skin']),int(dff_regulation.aggregate(['sum'])['Skin']), 
                    
###                0,0,1,0,1,0,0,0,0,  #Blood

               int(dff_attention.aggregate(['sum'])['Blood']),int(dff_load.aggregate(['sum'])['Blood']),int(dff_skills.aggregate(['sum'])['Blood']),
               int(dff_beliefs.aggregate(['sum'])['Blood']),int(dff_emotions.aggregate(['sum'])['Blood']),
               int(dff_habits.aggregate(['sum'])['Blood']),int(dff_traits.aggregate(['sum'])['Blood']),
               int(dff_knowledge.aggregate(['sum'])['Blood']),int(dff_regulation.aggregate(['sum'])['Blood']), 
                    
###                15,5,10,1,9,3,2,3,4,#EEG

               int(dff_attention.aggregate(['sum'])['EEG']),int(dff_load.aggregate(['sum'])['EEG']),int(dff_skills.aggregate(['sum'])['EEG']),
               int(dff_beliefs.aggregate(['sum'])['EEG']),int(dff_emotions.aggregate(['sum'])['EEG']),
               int(dff_habits.aggregate(['sum'])['EEG']),int(dff_traits.aggregate(['sum'])['EEG']),
               int(dff_knowledge.aggregate(['sum'])['EEG']),int(dff_regulation.aggregate(['sum'])['EEG']), 
                    
###                0,0,1,0,0,0,1,0,1,  #fMRI

               int(dff_attention.aggregate(['sum'])['fMRI']),int(dff_load.aggregate(['sum'])['fMRI']),int(dff_skills.aggregate(['sum'])['fMRI']),
               int(dff_beliefs.aggregate(['sum'])['fMRI']),int(dff_emotions.aggregate(['sum'])['fMRI']),
               int(dff_habits.aggregate(['sum'])['fMRI']),int(dff_traits.aggregate(['sum'])['fMRI']),
               int(dff_knowledge.aggregate(['sum'])['fMRI']),int(dff_regulation.aggregate(['sum'])['fMRI']), 
                    
###                1,0,1,1,0,0,0,0,0,  #NIRS

               int(dff_attention.aggregate(['sum'])['NIRS']),int(dff_load.aggregate(['sum'])['NIRS']),int(dff_skills.aggregate(['sum'])['NIRS']),
               int(dff_beliefs.aggregate(['sum'])['NIRS']),int(dff_emotions.aggregate(['sum'])['NIRS']),
               int(dff_habits.aggregate(['sum'])['NIRS']),int(dff_traits.aggregate(['sum'])['NIRS']),
               int(dff_knowledge.aggregate(['sum'])['NIRS']),int(dff_regulation.aggregate(['sum'])['NIRS']), 
                    
###                0,2,0,0,0,0,0,0,0, #fNIR

               int(dff_attention.aggregate(['sum'])['fNIR']),int(dff_load.aggregate(['sum'])['fNIR']),int(dff_skills.aggregate(['sum'])['fNIR']),
               int(dff_beliefs.aggregate(['sum'])['fNIR']),int(dff_emotions.aggregate(['sum'])['fNIR']),
               int(dff_habits.aggregate(['sum'])['fNIR']),int(dff_traits.aggregate(['sum'])['fNIR']),
               int(dff_knowledge.aggregate(['sum'])['fNIR']),int(dff_regulation.aggregate(['sum'])['fNIR']), 

### knowledge 	regulation 	attention	load	skills	beliefs 	emotions	habits	traits

###                23,14,19,    #cognitive
            int(dff.aggregate(['sum'])['attention']),int(dff.aggregate(['sum'])['load']),int(dff.aggregate(['sum'])['skills']),
                    
###                3,27,8,3,    #non-cognitve
            int(dff.aggregate(['sum'])['beliefs']),int(dff.aggregate(['sum'])['emotions']),
            int(dff.aggregate(['sum'])['habits']),int(dff.aggregate(['sum'])['traits']),
                    
###                5,7,         #meta-cognitive
            int(dff.aggregate(['sum'])['knowledge']),int(dff.aggregate(['sum'])['regulation']),

### Report	performance	feedback    Intervention
### "Monitoring States","Performance Estimation","Feedback / Notification","Adaptive System",
                    

###                36, 3, 6, 6,29, 2, 4, 4, 7, 1, 1, 3,# Constructs vs reported outcome
### Cognitive	Non-Cognitive	Meta-Cognitive
                
            int(dffc.aggregate(['sum'])['Report']),int(dffc.aggregate(['sum'])['performance']),
            int(dffc.aggregate(['sum'])['feedback']),int(dffc.aggregate(['sum'])['Intervention']),#Cognitive

            int(dffn.aggregate(['sum'])['Report']),int(dffn.aggregate(['sum'])['performance']),
            int(dffn.aggregate(['sum'])['feedback']),int(dffn.aggregate(['sum'])['Intervention']),#Non-Cognitive                    

            int(dffm.aggregate(['sum'])['Report']),int(dffm.aggregate(['sum'])['performance']),
            int(dffm.aggregate(['sum'])['feedback']),int(dffm.aggregate(['sum'])['Intervention']),#Meta-Cognitive                    

                    
###             ANS,CNS                57.5,42.5,
                    
               int(dff.aggregate(['sum'])['Facial'])+int(dff.aggregate(['sum'])['Eye'])+
                    int(dff.aggregate(['sum'])['Heart'])+int(dff.aggregate(['sum'])['Skin'])+
                    int(dff.aggregate(['sum'])['Blood']),##ANS
                    
               int(dff.aggregate(['sum'])['EEG'])+
                    int(dff.aggregate(['sum'])['fMRI'])+int(dff.aggregate(['sum'])['NIRS'])+
                    int(dff.aggregate(['sum'])['fNIR'])


               ],

    color =  [

               c0 , c0, c0,c0,c0, c1,c1,c1, c1,
                c2,c2,c2,c2,c2,c2,c2,c2,c2, #facial
                c3,c3,c3,c3,c3,c3,c3,c3,c3,
                c4,c4,c4,c4,c4,c4,c4,c4,c4,
                c5,c5,c5,c5,c5,c5,c5,c5,c5,
                c6,c6,c6,c6,c6,c6,c6,c6,c6,
                c7,c7,c7,c7,c7,c7,c7,c7,c7,
                c8,c8,c8,c8,c8,c8,c8,c8,c8,
                c9,c9,c9,c9,c9,c9,c9,c9,c9,
                c10,c10,c10,c10,c10,c10,c10,c10,c10,

                c20,c21,c22,    #cognitive
                c23,c24,c25,c26, #non-cognitve
                c27,c28,       #meta-cognitive

                c14,c15,c16,c17,c14,c15,c16,c17,c14,c15,c16,c17,
                #c14,c15,c16,c17,#Results
                c18,c18,

                ],



   )
        )

     )


    return {
       'data': traces,
       'layout':{
          'title':'Sankey diagram of findings in the NeuroIS studies in Higher Education'}

    }
###############################################################BarChart####################################################


@app.callback(
    Output('graph-with-select', 'figure'),
    [Input('year-select', 'value'),
    Input('measure-select', 'value'),
     Input('construct-select', 'value')])
def update_figure(selected_year,selected_measure,selected_construct):
    skip=0
    dff1=df[df['Pub Year'] < 2014]
    dff2=df[df['Pub Year'] < 2014]
    measure=selected_measure
    construct=selected_construct

    for i in selected_year:
        if i == 2019 :
            skip=1
        
    if skip==1 :
        dff = df[df['Pub Year'] < 2019]
        year='all years'
        pm='temp'
    if skip == 0:
        dff = df[df['Pub Year'].isin(selected_year)]
        year=selected_year
        measure=selected_measure
        construct=selected_construct
    for i in selected_measure:
        if i == 'Total' :
            measure='all measures'
            dff1=dff
        if i == 'Facial' :
            dff1 =dff1.append(dff[dff['Facial'] == 1])            
        if i == 'Eye' :
            dff1 =dff1.append(dff[dff['Eye'] == 1])
        if i == 'Heart' :
            dff1 =dff1.append(dff[dff['Heart'] == 1])
        if i == 'Skin' :
            dff1 =dff1.append(dff[dff['Skin'] > 0])
        if i == 'Blood' :
            dff1 =dff1.append(dff[dff['Blood'] == 1])
        if i == 'EEG' :
            dff1 =dff1.append(dff[dff['EEG'] == 1])
        if i == 'fMRI' :
            dff1 =dff1.append(dff[dff['fMRI'] == 1])
        if i == 'NIRS' :
            dff1 =dff1.append(dff[dff['NIRS'] == 1])
        if i == 'fNIR' :
            dff1 =dff1.append(dff[dff['fNIR'] == 1])
                 
    ##dff=dff1.drop_duplicates('Title')
##    	attention	load	skills	beliefs 	emotions	habits	traits knowledge	regulation
    for i in selected_construct:
        
        if i == 'Total' :
            construct='all constructs'
            dff2=dff1        
        if i == 'Attention' :
            
            dff2 =dff2.append(dff1[dff1['attention'] == 1])
            
        if i == 'Cognitive load' :
            
            dff2 =dff2.append(dff1[dff1['load'] == 1])
            
        if i == 'Skill' :
            
            dff2 =dff2.append(dff1[dff1['skills'] == 1])
            
        if i == 'Attitudes and beliefs' :
            
            dff2 =dff2.append(dff1[dff1['beliefs'] == 1])
            
        if i == 'Social and emotional qualities' :
            dff2 =dff2.append(dff1[dff1['emotions'] == 1])
        if i == 'Habits and processes' :
            dff2 =dff2.append(dff1[dff1['habits'] == 1])
        if i == 'Personality traits' :
            dff2 =dff2.append(dff1[dff1['traits'] == 1])
        if i == 'Knowledge about cognition' :
            dff2 =dff2.append(dff1[dff1['knowledge'] == 1])
        if i == 'Self-regulation of cognition' :
            dff2 =dff2.append(dff1[dff1['regulation'] == 1])

    dff=dff2.drop_duplicates('Title')

        
    traces = []
##    for i in filtered_df.continent.unique():
    
##        df_by_measure = filtered_df[filtered_df['continent'] == i]
    traces.append(dict(
            {'x': ['Facial',	'Eye',	'Heart',	'Skin',	'Blood',	'EEG',	'fMRI',	'NIRS',	'fNIR'],
              'y': [int(dff.aggregate(['sum'])['Facial']),int(dff.aggregate(['sum'])['Eye']),
                    int(dff.aggregate(['sum'])['Heart']),int(dff.aggregate(['sum'])['Skin']),
                    int(dff.aggregate(['sum'])['Blood']),int(dff.aggregate(['sum'])['EEG']),
                    int(dff.aggregate(['sum'])['fMRI']),int(dff.aggregate(['sum'])['NIRS']),
                    int(dff.aggregate(['sum'])['fNIR'])],
             'type': 'bar', 'name': 'selected_year',
             'marker':{'color':[c2, c3,c4,c5,c6,c7,c8,c9,c10]}
             },


        ),

                  )

    return {
       'data': traces,
      'layout':{
          'title':'The number of studies per neuro measurement instrument',#'Number of studies using {} to capture {} in {} = {}'.format(measure,construct,year,dff.count().Title),
          #{'The total number of studies using Neuro-measures','dff.count().Title'},
          'xaxis':{ 'title': 'Neuro-Measures'},
          'yaxis':{'title': 'Number of studies'}, #'range': [0, 12] if selected_year != 2019 else [0, 40]},
          'hovermode':'closest',
            'transition' : {'duration': 500},}

    }

################################################################################################@app.callback(
@app.callback(
    Output(component_id='text-title', component_property='children'),
    [Input('year-select', 'value'),
     Input('measure-select', 'value'),
     Input('construct-select', 'value')]
    )
def update_figure(selected_year,selected_measure,selected_construct):
    skip=0
    dff1=df[df['Pub Year'] < 2014]
    dff2=df[df['Pub Year'] < 2014]
    measure=selected_measure
    construct=selected_construct

    for i in selected_year:
        if i == 2019 :
            skip=1
        
    if skip==1 :
        dff = df[df['Pub Year'] < 2019]
        year='all years'
        pm='temp'
    if skip == 0:
        dff = df[df['Pub Year'].isin(selected_year)]
        year=selected_year
        measure=selected_measure
        construct=selected_construct
    for i in selected_measure:
        if i == 'Total' :
            measure='all measures'
            dff1=dff
        if i == 'Facial' :
            dff1 =dff1.append(dff[dff['Facial'] == 1])            
        if i == 'Eye' :
            dff1 =dff1.append(dff[dff['Eye'] == 1])
        if i == 'Heart' :
            dff1 =dff1.append(dff[dff['Heart'] == 1])
        if i == 'Skin' :
            dff1 =dff1.append(dff[dff['Skin'] > 0])
        if i == 'Blood' :
            dff1 =dff1.append(dff[dff['Blood'] == 1])
        if i == 'EEG' :
            dff1 =dff1.append(dff[dff['EEG'] == 1])
        if i == 'fMRI' :
            dff1 =dff1.append(dff[dff['fMRI'] == 1])
        if i == 'NIRS' :
            dff1 =dff1.append(dff[dff['NIRS'] == 1])
        if i == 'fNIR' :
            dff1 =dff1.append(dff[dff['fNIR'] == 1])
                 
    ##dff=dff1.drop_duplicates('Title')
##    	attention	load	skills	beliefs 	emotions	habits	traits knowledge	regulation
    for i in selected_construct:
        
        if i == 'Total' :
            construct='all constructs'
            dff2=dff1        
        if i == 'Attention' :
            
            dff2 =dff2.append(dff1[dff1['attention'] == 1])
            
        if i == 'Cognitive load' :
            
            dff2 =dff2.append(dff1[dff1['load'] == 1])
            
        if i == 'Skill' :
            
            dff2 =dff2.append(dff1[dff1['skills'] == 1])
            
        if i == 'Attitudes and beliefs' :
            
            dff2 =dff2.append(dff1[dff1['beliefs'] == 1])
            
        if i == 'Social and emotional qualities' :
            dff2 =dff2.append(dff1[dff1['emotions'] == 1])
        if i == 'Habits and processes' :
            dff2 =dff2.append(dff1[dff1['habits'] == 1])
        if i == 'Personality traits' :
            dff2 =dff2.append(dff1[dff1['traits'] == 1])
        if i == 'Knowledge about cognition' :
            dff2 =dff2.append(dff1[dff1['knowledge'] == 1])
        if i == 'Self-regulation of cognition' :
            dff2 =dff2.append(dff1[dff1['regulation'] == 1])

    dff=dff2.drop_duplicates('Title')

        
    nmy=int(dff.count().Title)
    if nmy > 1 :
        
        pm='{} studies use {} to capture {} in {}'.format(dff.count().Title,measure,construct,year)
    else :
        pm='{} study uses {} to capture {} in {}'.format(dff.count().Title,measure,construct,year)
                    
                    

                    
                    
    return pm

################################################################################################
@app.callback(
    Output('table', 'data'),
    [Input('year-select', 'value'),
    Input('measure-select', 'value'),
     Input('construct-select', 'value')])
def update_table(selected_year,selected_measure,selected_construct):
    skip=0
    dff1=df[df['Pub Year'] < 2014]
    dff2=df[df['Pub Year'] < 2014]
    measure=selected_measure
    construct=selected_construct

    for i in selected_year:
        if i == 2019 :
            skip=1
        
    if skip==1 :
        dff = df[df['Pub Year'] < 2019]
        year='all years'
        pm='temp'
    if skip == 0:
        dff = df[df['Pub Year'].isin(selected_year)]
        year=selected_year
        measure=selected_measure
        construct=selected_construct
    for i in selected_measure:
        if i == 'Total' :
            measure='all measures'
            dff1=dff
        if i == 'Facial' :
            dff1 =dff1.append(dff[dff['Facial'] == 1])            
        if i == 'Eye' :
            dff1 =dff1.append(dff[dff['Eye'] == 1])
        if i == 'Heart' :
            dff1 =dff1.append(dff[dff['Heart'] == 1])
        if i == 'Skin' :
            dff1 =dff1.append(dff[dff['Skin'] > 0])
        if i == 'Blood' :
            dff1 =dff1.append(dff[dff['Blood'] == 1])
        if i == 'EEG' :
            dff1 =dff1.append(dff[dff['EEG'] == 1])
        if i == 'fMRI' :
            dff1 =dff1.append(dff[dff['fMRI'] == 1])
        if i == 'NIRS' :
            dff1 =dff1.append(dff[dff['NIRS'] == 1])
        if i == 'fNIR' :
            dff1 =dff1.append(dff[dff['fNIR'] == 1])
                 
    ##dff=dff1.drop_duplicates('Title')
##    	attention	load	skills	beliefs 	emotions	habits	traits knowledge	regulation
    for i in selected_construct:
        
        if i == 'Total' :
            construct='all constructs'
            dff2=dff1        
        if i == 'Attention' :
            
            dff2 =dff2.append(dff1[dff1['attention'] == 1])
            
        if i == 'Cognitive load' :
            
            dff2 =dff2.append(dff1[dff1['load'] == 1])
            
        if i == 'Skill' :
            
            dff2 =dff2.append(dff1[dff1['skills'] == 1])
            
        if i == 'Attitudes and beliefs' :
            
            dff2 =dff2.append(dff1[dff1['beliefs'] == 1])
            
        if i == 'Social and emotional qualities' :
            dff2 =dff2.append(dff1[dff1['emotions'] == 1])
        if i == 'Habits and processes' :
            dff2 =dff2.append(dff1[dff1['habits'] == 1])
        if i == 'Personality traits' :
            dff2 =dff2.append(dff1[dff1['traits'] == 1])
        if i == 'Knowledge about cognition' :
            dff2 =dff2.append(dff1[dff1['knowledge'] == 1])
        if i == 'Self-regulation of cognition' :
            dff2 =dff2.append(dff1[dff1['regulation'] == 1])

    dff=dff2.drop_duplicates('Title')

    return dff.to_dict('records')
################################################################################################
##
##
##plt.scatter(np.ones_like(dfp), dfp, marker='o')
@app.callback(
    Output('graph-with-participant', 'figure'),
    [Input('year-select', 'value'),
    Input('measure-select', 'value'),
     Input('construct-select', 'value')])
def update_figure(selected_year,selected_measure,selected_construct):
    skip=0
    dff1=df[df['Pub Year'] < 2014]
    dff2=df[df['Pub Year'] < 2014]
    measure=selected_measure
    construct=selected_construct

    for i in selected_year:
        if i == 2019 :
            skip=1
        
    if skip==1 :
        dff = df[df['Pub Year'] < 2019]
        year='all years'
        pm='temp'
    if skip == 0:
        dff = df[df['Pub Year'].isin(selected_year)]
        year=selected_year
        measure=selected_measure
        construct=selected_construct
    for i in selected_measure:
        if i == 'Total' :
            measure='all measures'
            dff1=dff
        if i == 'Facial' :
            dff1 =dff1.append(dff[dff['Facial'] == 1])            
        if i == 'Eye' :
            dff1 =dff1.append(dff[dff['Eye'] == 1])
        if i == 'Heart' :
            dff1 =dff1.append(dff[dff['Heart'] == 1])
        if i == 'Skin' :
            dff1 =dff1.append(dff[dff['Skin'] > 0])
        if i == 'Blood' :
            dff1 =dff1.append(dff[dff['Blood'] == 1])
        if i == 'EEG' :
            dff1 =dff1.append(dff[dff['EEG'] == 1])
        if i == 'fMRI' :
            dff1 =dff1.append(dff[dff['fMRI'] == 1])
        if i == 'NIRS' :
            dff1 =dff1.append(dff[dff['NIRS'] == 1])
        if i == 'fNIR' :
            dff1 =dff1.append(dff[dff['fNIR'] == 1])
                 
    ##dff=dff1.drop_duplicates('Title')
##    	attention	load	skills	beliefs 	emotions	habits	traits knowledge	regulation
    for i in selected_construct:
        
        if i == 'Total' :
            construct='all constructs'
            dff2=dff1        
        if i == 'Attention' :
            
            dff2 =dff2.append(dff1[dff1['attention'] == 1])
            
        if i == 'Cognitive load' :
            
            dff2 =dff2.append(dff1[dff1['load'] == 1])
            
        if i == 'Skill' :
            
            dff2 =dff2.append(dff1[dff1['skills'] == 1])
            
        if i == 'Attitudes and beliefs' :
            
            dff2 =dff2.append(dff1[dff1['beliefs'] == 1])
            
        if i == 'Social and emotional qualities' :
            dff2 =dff2.append(dff1[dff1['emotions'] == 1])
        if i == 'Habits and processes' :
            dff2 =dff2.append(dff1[dff1['habits'] == 1])
        if i == 'Personality traits' :
            dff2 =dff2.append(dff1[dff1['traits'] == 1])
        if i == 'Knowledge about cognition' :
            dff2 =dff2.append(dff1[dff1['knowledge'] == 1])
        if i == 'Self-regulation of cognition' :
            dff2 =dff2.append(dff1[dff1['regulation'] == 1])

    dff=dff2.drop_duplicates('Title')
    dfp=dff[['Total ','Facial ','Eye ','Heart ','Skin ','Blood ','EEG ','fMRI ','NIRS ','fNIR ']]
    
##  c2='rgba(200,32,51,0.8)';
##c3='rgba(153,51,0,0.8)';
##c4='rgba(255,100,100,0.8)';
##c5='rgba(255,155,0,0.8)';
##c6='rgba(255,0,0,0.8)';
##
##c7='rgba(0,96,255,0.8)';
##c8='rgba(100,100,255,0.8)';
##c9='rgba(153,0,205,0.8)';
##c10='rgba(100,100,155,0.8)';

  
    Total = go.Box( y=dfp["Total "], name = "Total",
                    boxpoints = 'all', marker = dict(color = 'rgba(0,0,0,0.9)'),line = dict(
                        color = 'rgba(0,0,0,0.6)'),jitter = 1, pointpos = 0,)
    Facial = go.Box( y=dfp["Facial "], name = "Facial" ,
                    boxpoints = 'all', marker = dict(color = 'rgba(150,20,40,0.9)'),line = dict(
                        color = 'rgba(200,32,51,0.6)'),jitter = 1, pointpos = 0,)
    Eye = go.Box( y=dfp["Eye "], name = "Eye" ,
                    boxpoints = 'all', marker = dict(color = 'rgba(140,45,0,0.9)'),line = dict(
                        color = 'rgba(153,51,0,0.6)'),jitter = 1, pointpos = 0,)
    Heart = go.Box( y=dfp["Heart "], name = "Heart",  
                    boxpoints = 'all', marker = dict(color = 'rgba(200,90,90,0.9)'),line = dict(
                        color = 'rgba(255,100,100,0.6)'),jitter = 1, pointpos = 0,)
    Skin = go.Box( y=dfp["Skin "], name = "Skin" ,
                    boxpoints = 'all', marker = dict(color = 'rgba(250,150,0,1)'),line = dict(
                        color = 'rgba(255,155,0,0.6)'),jitter = 1, pointpos = 0,)
    Blood = go.Box( y=dfp["Blood "], name = "Blood" , 
                    boxpoints = 'all', marker = dict(color = 'rgba(200,0,0,0.9)'),line = dict(
                        color = 'rgba(255,0,0,0.6)'),jitter = 1, pointpos = 0,)
    EEG = go.Box( y=dfp["EEG "], name = "EEG"  ,
                    boxpoints = 'all', marker = dict(color = 'rgba(0,90,250,0.9)'),line = dict(
                        color = 'rgba(0,96,255,0.6)'),jitter = 1, pointpos = 0,)
    fMRI = go.Box( y=dfp["fMRI "], name = "fMRI"  ,
                    boxpoints = 'all', marker = dict(color = 'rgba(90,90,200,1)'),line = dict(
                        color = 'rgba(100,100,255,0.6)'),jitter = 1, pointpos = 0,)
    NIRS = go.Box( y=dfp["NIRS "], name = "NIRS"  ,
                    boxpoints = 'all', marker = dict(color = 'rgba(143,0,195,0.9)'),line = dict(
                        color = 'rgba(153,0,205,0.6)'),jitter = 1, pointpos = 0,)
    fNIR = go.Box( y=dfp["fNIR "], name = "fNIR"  ,
                    boxpoints = 'all', marker = dict(color = 'rgba(90,90,145,0.9)'),line = dict(
                        color = 'rgba(100,100,155,0.6)'),jitter = 1, pointpos = 0,)
    
##    data = [Facial,Eye,Heart,Skin,Blood,EEG,fMRI,NIRS,fNIR,Total]
                
                
    return { 'data': [Facial,Eye,Heart,Skin,Blood,EEG,fMRI,NIRS,fNIR,Total],
##       'data': traces,
       'layout':{
          'title':'Distribution of participants’ size in the selected papers for each neuro measurement instrument'}

    }

################################################################################################


if __name__ == '__main__':
    app.run_server(debug=True)
