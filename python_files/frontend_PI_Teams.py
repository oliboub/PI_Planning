#!/usr/bin/env python
# coding: utf-8

# # PI  Teams management

# ## Prerequisites

# In[1]:


import global_variables as g
g.init()
import os
import PySimpleGUI as sg
from backend_PI import * # Import tout ce qui est spécifique au projet
from frontend_PI import *

connect('PIPlanning')


# ------
# ## Create Team

# In[24]:


def create_team_gui(info='Info'):
    if g.DEBUG_OL >= 1:
        print('--- function: create_team_gui(',info,')')
    
    sg.set_options(element_padding=(5, 10))

    projects_list=list_projects()
    comboproj = []
    for project in projects_list:
        comboproj.append(project.ProjectName)
    if g.DEBUG_OL >= 2:
        print(comboproj)
        
    info_layout = [sg.T(info,font='Calibri 11',justification="left")]
 
    left_layout = [
        [sg.T('Project Selection', size=(20, 1),font='Calibri 11'), sg.Combo(comboproj,key='-PROJECT-',size=(20, 1),font='Calibri 11')],
        [sg.T('Team Name', size=(20, 1),font='Calibri 11'), sg.I(key='-TEAM-',font='Calibri 11')],
        [sg.T('Team Description', size=(20, 1),font='Calibri 11'), sg.I(key='-DESC-',font='Calibri 11')],
        #[sg.Ok(), sg.Cancel()]
    ]
    right_layout=[[sg.T('Select image'),
                 sg.I(key='-IMG-',enable_events=True),
                 sg.FileBrowse(file_types=(('All files',['*.jpeg','*.jpg','*.png']),("JPEG Files","*.jpeg"),("JPG Files","*.jpg"),("PNG Files","*.png")))],
                 [sg.Image(key='-PHOTO-', data=convert_to_bytes('../imagesDB/ilovemycompany.jpeg',resize=(250,250)))]]
    
#    layout=[[sg.Frame("Contact data",left_layout, vertical_alignment='center',pad=((10,10),(10,10))),sg.VerticalSeparator(),sg.Col(right_layout,element_justification='center')],
#           [sg.B('Add',enable_events=True),sg.Cancel()]]
    
    layout = [info_layout,[sg.Frame("Team Data", left_layout, vertical_alignment='top', pad=((10, 10), (10, 10))),
             sg.VerticalSeparator(), sg.Col(right_layout, element_justification='center')],
            [sg.B('Add', enable_events=True), sg.Cancel()]]
 

    window = MyWindow('Create Team', layout,finalize=True)
    window.my_move_to_center()
    logo=""
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            break
 
        elif event == '-IMG-':
            logo='../imagesDB/'+values['-IMG-'].split("/")[-1]
            if g.DEBUG_OL >= 2:
                print(logo)
            window['-PHOTO-'].update(data=convert_to_bytes(values['-IMG-'],resize=(250,250)))
 
            
        elif event == 'Add':
            for project1 in projects_list:
                if project1.ProjectName == values['-PROJECT-']:
                    projectID = project1.ProjectID
            description = values['-DESC-']
            team=values['-TEAM-']
#            print(projectID,description,team)
            if not logo:
                logo='../imagesDB/ilovemycompany.jpeg'
            if g.DEBUG_OL >= 2:
                print(logo)
                
            create_team(projectID,team, description, logo)
            layout1=[[sg.T('Team:',font='Calibri 11'),sg.T(team,font='Calibri 11',text_color='blue'),sg.T('for projet:',font='Calibri 11'),sg.T(values['-PROJECT-'],font='Calibri 11',text_color='blue'),sg.T(' créée.',font='Calibri 11')],
                    [sg.Ok()]]
            window1 = MyWindow('info', layout1,element_justification='c',finalize=True)
            window1.my_move_to_center()
            
            
            event, values = window1.read()
            if event == sg.WIN_CLOSED or event == 'Cancel' or event=="Ok":
                window1.close()
                window.close()
                break


# In[ ]:


#create_team_gui('Please enter informations regarding this team')


# ## List_all_teams_gui()

# In[2]:


def list_all_teams_gui(page,teams,info='info'):
    if g.DEBUG_OL >= 1:
        print('--- function: list_all_teams_gui(',page,teams,info,')')
 
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
        if g.DEBUG_OL >= 2:
            print('TeamID',team.TeamID,'\tProjectID',team.ProjectID)
        projectname = Projects.objects(ProjectID=team.ProjectID).first()
        if projectname is None:
            projectname='Non allocated'
        project=projectname.ProjectName
                
#        print(team.TeamLogo)
        if team.TeamLogo != None:
            photo=team.TeamLogo
        else:
            photo ='../imagesDB/ilovemycompany.jpeg'
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
        if g.DEBUG_OL >= 2:
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
                teams = list_teams_page(page,team.ProjectID)
                list_all_teams_gui(page,teams,'ceci est l"info de base')
        elif event1 == "<":
            if teams.has_prev:
                page -= 1
                window.close()
                teams = list_teams_page(page,team.ProjectID)
                list_all_teams_gui(page,teams,'ceci est l"info de base')
        elif event1 == "<<":
            if teams.has_prev:
                page = 1
                window.close()
                teams = list_teams_page(page,team.ProjectID)
                list_all_teams_gui(page,teams,'ceci est l"info de base')
        elif event1 == ">>":
            if teams.has_next:
                page = teams.pages
                window.close()
                teams = list_teams_page(page,team.ProjectID)
                list_all_teams_gui(page,teams,'ceci est l"info de base')


# In[ ]:


#list_all_teams_gui(1)


# ## Select teams by Project

# In[19]:


def select_project_gui(info='info'):
    if g.DEBUG_OL >= 1:
        print('--- function: select_project_gui(',info,')')
    projects_list=list_projects()
    
    comboproj = []
    for project in projects_list:
        comboproj.append(project.ProjectName)
    if g.DEBUG_OL >= 2:
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

