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

df = pd.read_csv('measures.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H1(children='Neuro-Information-Systems in Higher Education:'),
            html.H2(children='A Systematic Literature Review'),
            
html.Div([
    html.H3(children='Filter by',
            style={
                                    'width':'37%',
                                    'float':'left',
                                    'borderBottom': 'grey solid',
                                    'backgroundColor': 'rgb(250, 250, 250)',
                                    'padding': '10px 5px'
                                }
##            style={
##                                    'width':'37%',
##                                    'display': 'block',
##                                    #'float':'left',
##                                    'border': 'black solid',
##                                    'backgroundColor': 'rgb(250, 250, 250)',
##                                    'padding': '10px 7px'
##                                }
            ),
     html.Div([
            html.H5(children='Year:',style={'display': 'inline',}),
             dcc.RadioItems(
                            id='year-select',
                            options=[
                                        {'label': 'Total', 'value': 2019},
                                        {'label': '2018', 'value': 2018},
                                        {'label': '2017', 'value': 2017},
                                        {'label': '2016', 'value': 2016},
                                        {'label': '2015', 'value': 2015},
                                        {'label': '2014', 'value': 2014}
                                    ], 
                           value=2019,
                            labelStyle={'display': 'inline'}
                        ),],style={
                                    'width':'37%',
                                    #'float':'left',
                                    'borderBottom': ' grey solid',
                                    'backgroundColor': 'rgb(250, 250, 250)',
                                    'padding': '10px 5px'
                                }
         
              ),
     html.Div([
     dcc.Graph(id='graph-with-select'),
   
    ],style={'width':'62%','float':'right','display': 'block'}
    ),

    html.Div([
            html.H5(children='Measure:',style={'display': 'inline',}),
             dcc.RadioItems(
                            id='measure-select',
                            options=[
                        
              
                                        {'label': 'Total', 'value': 1},
                                        {'label': 'Facial', 'value': 2},
                                        {'label': 'Eye', 'value': 3},
                                        {'label': 'Heart', 'value': 4},
                                        {'label': 'Skin', 'value': 5},
                                        {'label': 'Blood', 'value': 6},
                                 
                                        {'label': 'EEG', 'value': 7},
                                        {'label': 'fMRI', 'value': 8},
                                        {'label': 'NIRS', 'value': 9},
                                        {'label': 'fNIR', 'value': 10}
                                    ], 
                           value=1,
                            labelStyle={'display': 'inline'}
                        ),],style={
                                    'width':'37%',
                                    #'float':'left',
                                    'borderBottom': 'grey solid',
                                    'backgroundColor': 'rgb(250, 250, 250)',
                                    'padding': '10px 5px'
                                }
         
                          ),
##    	attention	load	skills	beliefs 	emotions	habits	traits knowledge	regulation


    html.Div([
            html.H5(children='Construct:',style={'display': 'inline',}),
             dcc.RadioItems(
                            id='construct-select',
                            options=[
                        
              
                                        {'label': 'Total', 'value': 1},
                                        {'label': 'Attention', 'value': 2},
                                        {'label': 'Cognitive load', 'value': 3},
                                        {'label': 'Skill', 'value': 4},
                                        
                                        {'label': 'Attitudes and beliefs', 'value': 5},
                                        {'label': 'Social and emotional qualities', 'value': 6},                                 
                                        {'label': 'Habits and processes', 'value': 7},
                                        {'label': 'Personality traits', 'value': 8},
                                        
                                        {'label': 'Knowledge about cognition', 'value': 9},
                                        {'label': 'Self-regulation of cognition', 'value': 10}
                                    ], 
                           value=1,
                            labelStyle={'display': 'block'}
                        ),],style={
                                    'width':'37%',
                                    'float':'left',
                                    #'borderBottom': 'grey solid',
                                    'backgroundColor': 'rgb(250, 250, 250)',
                                    'padding': '10px 5px'
                                }
         
                          ),

     
 ],style={'display': 'inline'}
         ),
    
    
   
    html.Div([
    
    dcc.Graph(id='graph-with-sankey'),

    dash_table.DataTable(
        id='table',
        	
        			 		 

        columns=[
                  {"name":'Title', "id":'Title'},  
                  {"name":'Author/s', "id":'Author/s'},  
                  {"name":'Year', "id":'Pub Year'},  
                  {"name":'Neuro Measure/s', "id":'Q1.1.Neuro Measure/s'},
                  
                  {"name":'Other Measures', "id":'Q1.2.Behavioural  Measure/s'},  
                  {"name":'Study Design', "id":'Q2.2.Experiment type '},  
                  {"name":'Self-reports', "id":'Questionnaire'},  
                  {"name":'pretest & posttest', "id":'pretest & posttest'},  
                  {"name":'#session', "id":'session/observation'},  
                  {"name":'#Group', "id":'Group '},  
                  {"name":'Control group', "id":'Control group'},  
                  {"name":'Randomization', "id":'Randomization '},  

                ],
        style_data={
                    'whiteSpace': 'normal',
                    'border': ' solid blue',
                    'height': 'auto'
                    },
        fixed_rows={ 'headers': True, 'data': 0 },
       # fixed_columns={ 'headers': True, 'data': 3 },
        style_header={ 'border': ' solid black' },
       style_cell={'textAlign': 'left',},#'minWidth': '0px', 'maxWidth': '180px',},
        style_cell_conditional=[
            {'textAlign': 'left'},
        {'if': {'column_id': 'Pub Year'},
         'width': '1px'},
        {'if': {'column_id': 'Author/s'},
         'width': '1px'},
       {'if': {'column_id': 'Title'},
         'width': '1px'},
       {'if': {'column_id': 'Q1.1.Neuro Measure/s'},
         'width': '1px'},
       {'if': {'column_id': 'Q1.2.Behavioural  Measure/s'},
         'width': '1px'},
       {'if': {'column_id': 'Q2.2.Experiment type '},
         'width': '1px'},
       {'if': {'column_id': 'Questionnaire'},
         'width': '1px'},
       {'if': {'column_id': 'pretest & posttest'},
         'width': '3%'},
       {'if': {'column_id': 'session/observation'},
         'width': '1px'},
       {'if': {'column_id': 'Group '},
         'width': '1px'},
       {'if': {'column_id': 'Control group'},
         'width': '3%'},
       {'if': {'column_id': 'Randomization '},
         'width': '3%'},

    ]
           ) 
    ],style={'width':'100%','display': 'inline-block'}
             ),



],)


##########################################################SANKEY##################################################################################

@app.callback(
    Output('graph-with-sankey', 'figure'),
    [Input('year-select', 'value'),
    Input('measure-select', 'value'),
     Input('construct-select', 'value')])

def update_figure(selected_year,selected_measure,selected_construct):
    ss=int(selected_year)
    dff = df[df['Pub Year'] < 2019]
    if selected_year != 2019 :
        dff = df[df['Pub Year'] == ss]
    if selected_measure == 2 :
        dff = dff[dff['Facial'] == 1]
    if selected_measure == 3 :
        dff = dff[dff['Eye'] == 1]
    if selected_measure == 4 :
        dff = dff[dff['Heart'] == 1]
    if selected_measure == 5 :
        dff = dff[dff['Skin'] == 1]
    if selected_measure == 6 :
        dff = dff[dff['Blood'] == 1]
    if selected_measure == 7 :
        dff = dff[dff['EEG'] == 1]
    if selected_measure == 8 :
        dff = dff[dff['fMRI'] == 1]
    if selected_measure == 9 :
        dff = dff[dff['NIRS'] == 1]
    if selected_measure == 10 :
        dff = dff[dff['fNIR'] == 1]
##    	attention	load	skills	beliefs 	emotions	habits	traits knowledge	regulation
    if selected_construct == 2 :
        dff = dff[dff['attention'] == 1]
    if selected_construct == 3 :
        dff = dff[dff['load'] == 1]
    if selected_construct == 4 :
        dff = dff[dff['skills'] == 1]
    if selected_construct == 5 :
        dff = dff[dff['beliefs'] == 1]
    if selected_construct == 6 :
        dff = dff[dff['emotions'] == 1]
    if selected_construct == 7 :
        dff = dff[dff['habits'] == 1]
    if selected_construct == 8 :
        dff = dff[dff['traits'] == 1]
    if selected_construct == 9 :
        dff = dff[dff['knowledge'] == 1]
    if selected_construct == 10 :
        dff = dff[dff['regulation'] == 1]

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
      if ((selected_year > 2018) & (selected_measure < 2) & (selected_construct < 2)) else  [],
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
      if ((selected_year > 2018) & (selected_measure < 2) & (selected_construct < 2)) else
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


    ss=int(selected_year)
    dff = df[df['Pub Year'] < 2019]
    year='all years'
    measure='all measures'
    construct='all constructs'
    if selected_year != 2019 :
        dff = df[df['Pub Year'] == ss]
        year=selected_year
    if selected_measure == 2 :
        dff = dff[dff['Facial'] == 1]
        measure='Facial'
    if selected_measure == 3 :
        dff = dff[dff['Eye'] == 1]
        measure='Eye'
    if selected_measure == 4 :
        dff = dff[dff['Heart'] == 1]
        measure='Heart'
    if selected_measure == 5 :
        dff = dff[dff['Skin'] == 1]
        measure='Skin'
    if selected_measure == 6 :
        dff = dff[dff['Blood'] == 1]
        measure='Blood'
    if selected_measure == 7 :
        dff = dff[dff['EEG'] == 1]
        measure='EEG'
    if selected_measure == 8 :
        dff = dff[dff['fMRI'] == 1]
        measure='fMRI'
    if selected_measure == 9 :
        dff = dff[dff['NIRS'] == 1]
        measure='NIRS'
    if selected_measure == 10 :
        dff = dff[dff['fNIR'] == 1]
        measure='fNIR'
##    	attention	load	skills	beliefs 	emotions	habits	traits knowledge	regulation
    if selected_construct == 2 :
        dff = dff[dff['attention'] == 1]
        construct='Attention'
    if selected_construct == 3 :
        dff = dff[dff['load'] == 1]
        construct='Cognitive load'
    if selected_construct == 4 :
        dff = dff[dff['skills'] == 1]
        construct='Skill'
    if selected_construct == 5 :
        dff = dff[dff['beliefs'] == 1]
        construct='Attitudes and beliefs'
    if selected_construct == 6 :
        dff = dff[dff['emotions'] == 1]
        construct='Social and emotional qualities'
    if selected_construct == 7 :
        dff = dff[dff['habits'] == 1]
        construct='Habits and processes'
    if selected_construct == 8 :
        dff = dff[dff['traits'] == 1]
        construct='Personality traits'
    if selected_construct == 9 :
        dff = dff[dff['knowledge'] == 1]
        construct='Knowledge about cognition'
    if selected_construct == 10 :
        dff = dff[dff['regulation'] == 1]
        construct='Self-regulation of cognition'


        
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
          'title':'Number of studies using {} to capture {} in {} = {}'.format(measure,construct,year,dff.count().Title),
          #{'The total number of studies using Neuro-measures','dff.count().Title'},
          'xaxis':{ 'title': 'Neuro-Measures'},
          'yaxis':{'title': 'Number of studies'}, #'range': [0, 12] if selected_year != 2019 else [0, 40]},
          'hovermode':'closest',
            'transition' : {'duration': 4500},}

    }

################################################################################################
@app.callback(
    Output('table', 'data'),
    [Input('year-select', 'value'),
    Input('measure-select', 'value'),
     Input('construct-select', 'value')])
def update_table(selected_year,selected_measure,selected_construct):
            ss=int(selected_year)
            dff = df[df['Pub Year'] < 2019]
            if selected_year != 2019 :
                dff = df[df['Pub Year'] == ss]
            if selected_measure == 2 :
                dff = dff[dff['Facial'] == 1]
            if selected_measure == 3 :
                dff = dff[dff['Eye'] == 1]
            if selected_measure == 4 :
                dff = dff[dff['Heart'] == 1]
            if selected_measure == 5 :
                dff = dff[dff['Skin'] == 1]
            if selected_measure == 6 :
                dff = dff[dff['Blood'] == 1]
            if selected_measure == 7 :
                dff = dff[dff['EEG'] == 1]
            if selected_measure == 8 :
                dff = dff[dff['fMRI'] == 1]
            if selected_measure == 9 :
                dff = dff[dff['NIRS'] == 1]
            if selected_measure == 10 :
                dff = dff[dff['fNIR'] == 1]
##    	attention	load	skills	beliefs 	emotions	habits	traits knowledge	regulation
            if selected_construct == 2 :
                dff = dff[dff['attention'] == 1]
            if selected_construct == 3 :
                dff = dff[dff['load'] == 1]
            if selected_construct == 4 :
                dff = dff[dff['skills'] == 1]
            if selected_construct == 5 :
                dff = dff[dff['beliefs'] == 1]
            if selected_construct == 6 :
                dff = dff[dff['emotions'] == 1]
            if selected_construct == 7 :
                dff = dff[dff['habits'] == 1]
            if selected_construct == 8 :
                dff = dff[dff['traits'] == 1]
            if selected_construct == 9 :
                dff = dff[dff['knowledge'] == 1]
            if selected_construct == 10 :
                dff = dff[dff['regulation'] == 1]

            return dff.to_dict('records')



################################################################################################



if __name__ == '__main__':
    app.run_server(debug=True)
