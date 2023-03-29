#!/usr/bin/env python
# coding: utf-8

# ## PI Members Management

# In[ ]:


import PySimpleGUI as sg
from backend_PI import * # Import tout ce qui est spécifique au projet

connect('PIPlanning')


# ## create_member_gui

# In[ ]:


def create_member_gui(info='Info'):
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
            teams_list=list_teams(project)
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





# In[ ]:


print(__name__,'imported')

