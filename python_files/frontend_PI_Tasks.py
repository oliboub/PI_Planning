#!/usr/bin/env python
# coding: utf-8

# # Sprint Tasks management

# ## Prerequisites

# In[ ]:


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


# In[ ]:


from frontend_PI_Utils import *


# In[ ]:


connect('PIPlanning')


# ------
# ## Create Tasks

# In[ ]:


def create_task_gui(info='Info'):
    sg.set_options(element_padding=(5, 10))

    projects_list=list_projects()
    comboproj = []
    for project in projects_list:
        comboproj.append(project.ProjectName)
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
#        print(event,values)
        
        if event == sg.WIN_CLOSED or event == 'Cancel':
#            print(event)
            window.close()
            break
 
        elif '-PROJ-' in event:
#           print(values['-PROJ-'])
            project=values['-PROJ-']
            list_teams = []
            teams_list=list_teams_by_project(project)
            for i in range(len(teams_list)):
#                print(teams_list[i][1])
                list_teams.append(teams_list[i][1])
            print(list_teams)
            window['-TXTTEAM-'].update(visible=True)
            window['-TEAM-'].update(values=list_teams,visible=True)
            

              
        elif '-TEAM-' in event:
            team=values['-TEAM-']
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


# In[ ]:


#create_task_gui("Creation d'une tache dans un project et affectée à une équipe")


# ## List All Tasks

# In[ ]:


def list_all_teams_gui(page,teams,info='info'):
#    global page
    sg.set_options(element_padding=(5, 5))
#    list_teams=list_teams_all()
    layout = [[sg.T(info,font='Calibri 11',justification="left")],
              [sg.T('Team Name',font='Calibri 11', size=(20, 1)),
               sg.T('Team Description',font='Calibri 11', size=(30, 1)),
               sg.T('Associated Project',font='Calibri 11', size=(20, 1)),
               sg.T('Team Logo',font='Calibri 11')]]
    idx=0
    for team in teams.items:
        print(team.TeamID,team.ProjectID)
        projectname = Projects.objects(ProjectID=team.ProjectID).first()
        if projectname is None:
            projectname='Non allocated'
        project=projectname.ProjectName
                
#        print(team.TeamLogo)
        if team.TeamLogo != None:
            photo=team.TeamLogo
        else:
            photo ='imagesDB/ilovemycompany.jpeg'
#        print(TeamPhoto)

        row = [sg.I(team.TeamName,disabled=True,font='Calibri 11', size=(20,1)),
               sg.I(team.TeamDescription,disabled=True, font='Calibri 11',size=(30,1)),
               sg.I(project,disabled=True, font='Calibri 11',size=(20,1)),
               sg.Image(key='-PHOTO-', data=convert_to_bytes(photo, resize=(75, 75)))],
        layout.append(row)
        idx+=1
        
    pagination = [[sg.B('<<', disabled=not teams.has_prev),
                   sg.B("<", disabled=not teams.has_prev),
                   sg.T(text=page, key='-PAGE-', size=(2, 1)),
                   sg.B(">", disabled=not teams.has_next),
                   sg.B(">>", disabled=not teams.has_next)
                   ]]
    layout += [[sg.Col(pagination, justification='right')]]
    layout += [[sg.B('Return')]]
               
    window = MyWindow('List of Teams', layout,keep_on_top=True, element_justification = 'center',finalize=True)
    window.my_move_to_center()
    
    while True:
        event1, values1 = window.read()
        print(event1,values1)
        if event1 == sg.WIN_CLOSED or event1 == 'Return':
#            print('event1',event1)
            window.close()
            return(None)
            break  
        elif event1 == ">":
            if teams.has_next:
                page += 1
                window.close()
                teams = list_teams_page(page)
                list_all_teams_gui(page,teams,'ceci est l"info de base')
        elif event1 == "<":
            if teams.has_prev:
                page -= 1
                window.close()
                teams = list_teams_page(page)
                list_all_teams_gui(page,teams,'ceci est l"info de base')
        elif event1 == "<<":
            if teams.has_prev:
                page = 1
                window.close()
                teams = list_teams_page(page)
                list_all_teams_gui(page,teams,'ceci est l"info de base')
        elif event1 == ">>":
            if teams.has_next:
                page = teams.pages
                window.close()
                teams = list_teams_page(page)
                list_all_teams_gui(page,teams,'ceci est l"info de base')


# ## Select teams by Project

# In[ ]:


def select_project_gui(info='info'):
    projects_list=list_projects()
    
    comboproj = []
    for project in projects_list:
        comboproj.append(project.ProjectName)
    print(comboproj)
        
    layout = [
        [sg.T(info,font='Calibri 11',justification="left")],
        [sg.T('Project Selection', size=(20, 1),font='Calibri 11'), sg.Combo(comboproj,key='-PROJECT-',size=(20, 1),font='Calibri 11')],
        [sg.Ok(), sg.Cancel()]
    ]
    window = MyWindow('Select Project', layout,finalize=True)
    window.my_move_to_center()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            break
        elif event == 'Ok':
            projectname=values['-PROJECT-']
            projects = Projects.objects(ProjectName=projectname).first()
            projectid=projects.ProjectID
            
#            print(__name__,projectname,projectid,'\n----------\n')
            window.close()

            return(projectid,projectname)


# page = 1
# projectid=None
# projectid,projectname=select_project_gui() # a lan cer pour chercher les equipes d'un projet
# 
# print(__name__,projectid,projectname)
# print(__name__,'projectname:',projectname)
# teams=list_teams_page(1,projectid)
# for a in teams.items:
#     print(a.TeamName,'\t',a.TeamDescription,'\t',a.TeamLogo,'\t',a.ProjectID)
# if projectid == None:
#     info='Liste de toutes les equipes'
# else:
#     info='Liste de toutes les equipes du projet '+ projectname
# list_all_teams_gui(page,teams,info)

# In[ ]:


print(os.getcwd(),__name__,'imported')

