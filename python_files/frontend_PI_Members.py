#!/usr/bin/env python
# coding: utf-8

# ## PI Members Management

# In[1]:


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


# ## list_members_gui(page,members,info='info')
# **WIP**

# In[4]:


def list_members_gui(page,members,info='info'):
    if g.DEBUG_OL >= 1:
        print('--- function: list_members_gui(',page,members,info,')')
 
    #    global page
    sg.set_options(element_padding=(5, 5))
#    list_teams=list_teams_all()
    layout = [[sg.T(info,font='Calibri 11',justification="left")],
              [sg.T('Member Name',font='Calibri 11', size=(20, 1)),
               sg.T('Member Alias',font='Calibri 11', size=(30, 1)),
               sg.T('Member Role',font='Calibri 11', size=(20, 1)),
               sg.T('Member Email',font='Calibri 11')]]
    idx=0
    for memnber in members.items:
        if g.DEBUG_OL >= 2:
            print('MemberID',member[0],'\tProjectID',member[6],'\tTeam:',member[7])

        row = [sg.I(member[1],disabled=True,font='Calibri 11', size=(20,1)),
               sg.I(member[2],disabled=True, font='Calibri 11',size=(30,1)),
               sg.I(member[9],disabled=True, font='Calibri 11',size=(20,1)),
               sg.I(member[5],disabled=True, font='Calibri 11',size=(20,1)),]
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


print(__name__,'imported')

