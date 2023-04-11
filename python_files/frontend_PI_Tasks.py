#!/usr/bin/env python
# coding: utf-8

# # Sprint Tasks management

# ## Prerequisites

# In[1]:


import os
import time
import bcrypt
from datetime import datetime
import PySimpleGUI as sg
import global_variables as g
g.init()
#time.sleep(1)
from backend_PI_Utils import * # Import tout ce qui est spécifique au projet
from backend_PI_mongo_model import * # Import tout ce qui est spécifique au projet
time.sleep(1)
from backend_PI_Members import * # Import tout ce qui est spécifique au projet
from backend_PI_Projects import * # Import tout ce qui est spécifique au projet
from backend_PI_Roles import * # Import tout ce qui est spécifique au projet
from backend_PI_Tasks import * # Import tout ce qui est spécifique au projet
from backend_PI_Teams import * # Import tout ce qui est spécifique au projet


# In[2]:


from frontend_PI_Utils import *


# In[3]:


connect('PIPlanning')


# ------
# ## Create Tasks

# In[12]:


def create_task_gui(memberid,info='Info'):
    if g.DEBUG_OL >= 1:    
        print('fonction: create_task_gui(',memberid,info,')')
 
    sg.set_options(element_padding=(5, 10))

    projects_list=list_projects()
    comboproj = []
    for project in projects_list:
        comboproj.append(project.ProjectName)
    if g.DEBUG_OL >= 1: 
        print(comboproj)
    
    team=[]
    combomembers=[]
    
    info_layout = [sg.T(info,font='Calibri 11',justification="left")]
 
    left_layout = [
        [sg.T('Project Selection', size=(20, 1),font='Calibri 11'), sg.Combo(comboproj,key='-PROJ-',enable_events=True,size=(20, 1),font='Calibri 11')],
        [sg.T('Team Name', size=(20, 1),key='-TXTTEAM-',font='Calibri 11',visible=False), sg.Combo(team,key='-TEAM-',enable_events=True,visible=False,size=(20, 1),font='Calibri 11')],
    ]
    
    bottom_layout=[[sg.T('Task Name',key='-TNAME-',size=(15,1),font='Calibri 11',visible=False),
                    sg.I("",key='-TNAMEI-',visible=False,size=(20,1))],
                  [sg.T('Task Member',key='-TMEMBER-',size=(15,1),font='Calibri 11',visible=False),
                   sg.Combo(combomembers,key='-TMEMBERI-',enable_events=True,size=(20, 1),font='Calibri 11',visible=False)]
                  ]
    
#    layout = [info_layout,[sg.Frame("Select perimeter", left_layout, vertical_alignment='top', pad=((10, 10), (10, 10)))],
#            [sg.B('Add', enable_events=True), sg.Cancel()]]
             
    layout = [info_layout,[sg.Frame("Select perimeter", left_layout, vertical_alignment='top', pad=((10, 10), (10, 10)))],
              [sg.Frame("Task", bottom_layout,key='-TASKS-', vertical_alignment='top',pad=((10, 10), (10, 10)),visible=False)],
              [sg.B('Add', enable_events=True), sg.Cancel()]]
        
    window = MyWindow('Create task', layout,finalize=True)
    window.my_move_to_center()
    
    while True:
        event, values = window.read()
        if g.DEBUG_OL >= 1:
            print(event,values)
        
        if event == sg.WIN_CLOSED or event == 'Cancel':
#            print(event)
            window.close()
            break
 
        elif '-PROJ-' in event:
            if g.DEBUG_OL >= 1: 
                print(values['-PROJ-'])
            project=values['-PROJ-']
            teams_list = []
            teams=[]
            teams_list=list_teams(project)
            for i in range(len(teams_list)):
#                print(teams_list[i][1])
                teams.append(teams_list[i][1])
            print(teams)
            window['-TXTTEAM-'].update(visible=True)
            window['-TEAM-'].update(values=teams,visible=True)
            

              
        elif '-TEAM-' in event:
            team=values['-TEAM-']
            if g.DEBUG_OL >= 1: 
                print(team)

            tasks_lists=list_tasks(project,team,'All','All')
            
            combomembers=query_members_by_team(team)
            print(combomembers)
            
            titre='Lists of tasks for project: '+project+' and team:'+team
            window['-TASKS-'].update(value=titre,visible=True)
            window['-TNAME-'].update(visible=True)
            window['-TNAMEI-'].update(visible=True)
            window['-TMEMBER-'].update(visible=True)
            window['-TMEMBERI-'].update(values=combomembers,visible=True)
            
        elif event == 'Add':
            print(event,values)
            pass


# In[13]:


#memberid=1
#create_task_gui(memberid,"Creation d'une tache dans un project et affectée à une équipe")


# ## List All Tasks

# In[ ]:


def list_all_tasks_gui(memberid,page,teams,info='info'):
    if g.DEBUG_OL >= 1:    
        print('fonction: list_all_tasks_gui(',memberid,info,')')

    sg.set_options(element_padding=(5, 5))
#


# In[ ]:


if g.DEBUG_OL >= 1:
    print(os.getcwd(),__name__,'imported')

