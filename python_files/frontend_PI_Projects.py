#!/usr/bin/env python
# coding: utf-8

# ## PI Project Management

# In[ ]:


import os
import PySimpleGUI as sg
from backend_PI import * # Import tout ce qui est spécifique au projet
from frontend_PI import *

connect('PIPlanning')


# ### Create project

# In[ ]:


def create_project_gui(info):
    layout = [
        [sg.T(info,font='Calibri 12',justification="left")],
        [sg.T('project Name', size=(20, 1)), sg.I(key='-PROJECT-')],
        [sg.T('Project Description', size=(20, 1)), sg.I(key='-DESC-')],
        [sg.Ok(), sg.Cancel()]
    ]
    window = MyWindow('Create Project', layout,finalize=True)
    window.my_move_to_center()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            break
        elif event == 'Ok':
            project = values['-PROJECT-']
            description = values['-DESC-']
            create_project(project, description)
            layout1=[[sg.T('Projet:',font='Calibri 12'),sg.T(values['-PROJECT-'],font='Calibri 12'),sg.T(' créé.',font='Calibri 12')],
                    [sg.Ok()]]
            window1 = MyWindow('info', layout1, element_justification='c',finalize=True)
            window1.my_move_to_center()
            
            event, values = window1.read()
            if event == sg.WIN_CLOSED or event == 'Cancel' or event=="Ok":
                window1.close()
                window.close()
                break


# ### List Projects

# In[ ]:


def list_projects_gui(info):
    print('fonction: list_projects_gui(',info,')')
    layout = []
    projects_list=list_projects()
#    print(projects_list)

    layout = [[sg.T(info,font='Calibri 12',justification="left")],
              [sg.T('Select',size=(5,1)),sg.T('Project Name',size=(15, 1)),sg.T('Description', size=(40, 1)),sg.T('Creation Date',size=(40, 1))]]
    for project in projects_list:
#        print(project.ProjectName)
        row = [[sg.Radio('', "RADIO1", key=f'-RADIO-{project.ProjectID}'),
                sg.I(project.ProjectName, key=f'-PROJ-{project.ProjectID}', disabled=True, size=(15, 1), text_color='black'),
                sg.I(project.ProjectDescription, key=f'-DESC-{project.ProjectID}', enable_events=True, size=(40, 1), text_color='black'),
                sg.I(project.CreationDate, key=f'-CREAT-{project.ProjectID}', enable_events=True, size=(40, 1), text_color='black')]]
        layout.append(row)

    layout += [[sg.B('Select')]]
               
    window = MyWindow('List of Projects', layout,keep_on_top=True, element_justification = 'center',finalize=True)
    window.my_move_to_center()
    
    while True:
        event1, values1 = window.read()
        print(event1,values1)
        if event1 == sg.WIN_CLOSED or event1 == 'Cancel':
            print('Exit')
            window.close()
            return(None,None,None)
            break              
#        if event1 == '-RADIO-':
#            print('Radio',event1,values1)
            
#        elif '-DESC-' in event1:
#            print(values1)
        
        elif event1 == 'Select':
#            if '-SEL-' == "None":
#                sg.popup_error("Merci de sélectionner un projet!")
#            print(event1,values1)
            for k, v in values1.items():
#                print(k,v)
                if v == True:
                    print('True',k, v)
                    a=int(k.split("-")[-1])
#                    print(a)
                    projectselected = query_project_name_from_ID(a)
                    ActualProjectID=projectselected.ProjectID
                    ActualProjectName=projectselected.ProjectName
                    ActualProjectDesc=projectselected.ProjectDescription
#                    print(ActualProjectName,ActualProjectDesc)
                    window.close()
                    return(ActualProjectID,ActualProjectName,ActualProjectDesc)


# ### Archive project

# In[ ]:


def archive_project_gui(info):
    print('fonction: list_projects_gui(',info,')')
    layout = []
    projects_list=list_projects()
    
#    print(projects_list)

    layout = [[sg.T(info,font='Calibri 12',justification="left")],
              [sg.T('Archive',size=(5,1)),sg.T('Project Name',size=(15, 1)),sg.T('Description', size=(40, 1)),sg.T('Creation Date',size=(40, 1))]]
    for project in projects_list:
#        print(project.ProjectName)
        row = [[sg.Radio('', "RADIO1", key=f'-RADIO-{project.ProjectID}'),
                sg.I(project.ProjectName, key=f'-PROJ-{project.ProjectID}', disabled=True, size=(15, 1), text_color='black'),
                sg.I(project.ProjectDescription, key=f'-DESC-{project.ProjectID}', enable_events=True, size=(40, 1), text_color='black'),
                sg.I(project.CreationDate, key=f'-CREAT-{project.ProjectID}', enable_events=True, size=(40, 1), text_color='black')]]
        layout.append(row)

    layout += [[sg.B('Select'), sg.Cancel()]]
               
    window = MyWindow('List of Projects', layout,keep_on_top=True, element_justification = 'center',finalize=True)
    window.my_move_to_center()
    
    while True:
        event1, values1 = window.read()
        print(event1,values1)
        if event1 == sg.WIN_CLOSED or event1 == 'Cancel':
#            print('event1',event1)
            window.close()
            return(None)
            break              

        elif '-DESC-' in event1:
            print(values1)
        
        elif event1 == 'Select':
            for k, v in values1.items():
                print(k,v)
                if v == True:
#                    print('True',k, v)
                    a=int(k.split("-")[-1])
#                    print(a)
                    for project1 in projects_list:
                        if project1.ProjectID == a:
                            print(project1.ProjectID,project1.ProjectName,project1.Archived)
                            ArchivedProjectName=project1.ProjectName
                            response = archive_project(project1.ProjectID)
                            print(response)
                            layout1=[[sg.T('Projet:',font='Calibri 12'),sg.T(ArchivedProjectName,font='Calibri 12'),sg.T(' archivé.',font='Calibri 12')],[sg.Ok()]]
                            window1 = MyWindow('info', layout1,element_justification='c',keep_on_top=True,finalize=True)
                            window1.my_move_to_center()
                            
                            event2, values2 = window1.read()
                            if event2 == sg.WIN_CLOSED or event2 == 'Cancel' or event2=="Ok":
                                    window.close()
                                    window1.close()
                            return(ArchivedProjectName)


# In[ ]:


print(os.getcwd(),__name__,'imported')

