#!/usr/bin/env python
# coding: utf-8

# # PI  Teams management

# ## Prerequisites

# In[1]:


import os
import time
import bcrypt
from datetime import datetime
import PySimpleGUI as sg
import global_variables as g
from operator import itemgetter
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
# ## Create Team

# In[ ]:


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
        
    info_layout = [sg.T(info,font=g.FONT,justification="left")]
 
    left_layout = [
        [sg.T('Project Selection', size=(20, 1),font=g.FONT), sg.Combo(comboproj,key='-PROJECT-',size=(20, 1),font=g.FONT)],
        [sg.T('Team Name', size=(20, 1),font=g.FONT), sg.I(key='-TEAM-',font=g.FONT)],
        [sg.T('Team Description', size=(20, 1),font=g.FONT), sg.I(key='-DESC-',font=g.FONT)],
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
                
            id=create_team(projectID,team, description, logo)
            if g.DEBUG_OL >= 2:
                print('New team created with id:',id)
            sg.popup('New team '+values['-TEAM-']+' created with id: '+str(id),title="info",auto_close=True, auto_close_duration=3,)
            window.close()
            break


# In[ ]:


#create_team_gui('Please enter informations regarding this team')


# ## List_teams_gui(project=None,page=1,linespage=5,order1=8,order2=1,order3=3,info='info')

# In[8]:


def list_teams_gui(project=None,page=1,linespage=5,order1=1,order2=2,order3=4,info='info'):
    if g.DEBUG_OL >= 1:
        print('--- function: list_teams_gui(',project,page,linespage,order1,order2,order3,info,')')
 
    projects_list=list_projects()
    comboproj = []
    for project1 in projects_list:
        comboproj.append(project1.ProjectName)
    if g.DEBUG_OL >= 2:
        print(comboproj)
 
    team=[]  
    teams1=[]
    photo=''
    teamstotal=[]
    teams=[]
    order1=int(order1)
    order2=int(order2)
    order3=int(order3)

     
    sg.set_options(element_padding=(5, 5))
    if project == None:
        teams1=list_teams()
    else:
        teams1=list_teams(project)
        if len(teams1) == 0:
            sg.popup(project+' has no teams yet', title="warning",auto_close=True, auto_close_duration=3,)
            teams1=list_teams()
            
    idx=0
    for team in teams1:
        if g.DEBUG_OL >= 2:
            print('ProjectID:',team[0],'\tProjectName:',team[1],'\tTeamID:',team[2],'\'TeamName:',team[3],'\tTeamDescription:',team[4],'\tTeamLogo:',team[5],'\tLastUpdate:',team[6],'\tArchived:',team[7])

    
    teamstotal=sorted(teams1, key = itemgetter(order1, order2, order3))

    items=len(teamstotal)

    start=page*linespage-linespage
    end=start+linespage
    if end > items:
        end = items
    a=0
 
    if g.DEBUG_OL >=2:
        print('items:',items,'\tstart:',start,'\tend:',end)
    

    for i in range(start,end):
        teams.append(teamstotal[i])
        if g.DEBUG_OL >= 2:
            print(teams[a])
        a=+1
    
        
    if project == None:
        titlewindows='List of Teams for all projects'
    else:
        titlewindows='List of Teams for the project: '+ project
        
    sg.set_options(element_padding=(5, 5))
    
    layout = [[sg.T(info,font=g.FONT,justification="left")],
              [sg.T('Project Name',font=g.FONT,key='-PFILTER-',enable_events=True, size=(15, 1)),
               sg.T('Team Name',font=g.FONT,key='-TFILTER-',enable_events=True, size=(15, 1)),
               sg.T('Team Description',font=g.FONT,size=(35, 1)),
               sg.T('Team Logo',font=g.FONT, size=(10, 1)),
               sg.T('Last Update',font=g.FONT,key='-LFILTER-',enable_events=True, size=(18, 1)),
               sg.T('Update',font=g.FONT,size=(10, 1)),
               sg.T(' ',font=g.FONT,size=(5, 1)),
               sg.T('Status',font=g.FONT,size=(10, 1))
              ],
             [sg.Combo(comboproj,key='-PROJECT-',enable_events=True,size=(15, 1),font=g.FONT),sg.T(" ",size=(118, 1),font=g.FONT)]
             ]
    
    idx=0
    for team in teams:
        if g.DEBUG_OL >= 2:
            print('TeamID',team[2],'\tProjectID',team[0],'\tTeam:',team[2])

            
        if team[7] is False:
            status='Active'
            FONT1=g.FONT
            bfcolor='white'
            bbcolor='green'
            
        else:
            status='Archived'
            FONT1=g.FONT+' italic'
            bfcolor='white'
            bbcolor='firebrick3'
 
            
        row = [sg.I(team[1],enable_events=True,key=f'-PNAME-{team[2]}', font=g.FONT, size=(15,1)),
               sg.I(team[3],enable_events=True,key=f'-TNAME-{team[2]}', font=g.FONT, size=(15,1)),
               sg.I(team[4],enable_events=True,key=f'-TDESC-{team[2]}', font=g.FONT,size=(35,1)),
               sg.Image(enable_events=True,key=f'-PHOTOIMG-{team[2]}', data=convert_to_bytes(team[5], resize=(75, 75))),
               sg.I(team[5],enable_events=False,visible=False,key=f'-PHOTO-{team[2]}'),
               sg.I(team[0],enable_events=False,visible=False,key=f'-PID-{team[2]}'),
               sg.I(team[6],disabled=True, font=g.FONT,size=(18,1)),
               sg.B('Update',enable_events=True, key=f'-UPDT-{team[2]}',font=g.FONT,button_color=('white','darkblue'),size=(10,1)),
               sg.T(' ',font=g.FONT,size=(5, 1)),
               sg.B(status, enable_events=True,key=f'-ARCH-{team[2]}',font=FONT1,button_color=(bfcolor,bbcolor),size=(10,1)),

              ]
        layout.append(row)
        idx+=1
   
    
    teamqtt= [[sg.T('Total teams found: ',font=g.FONT, size=(24, 1)),
               sg.I(items,key='-TFOUND-',enable_events=False,disabled=True,visible=True,size=(10,1))]
                  ]
    
    displaylines= [[sg.T('Displayed Lines:',font=g.FONT, size=(22, 1)),sg.I(linespage,key='-DLINES-',enable_events=True,visible=True,size=(10,1))]
                  ]
    
    pagination = [[sg.B('<<', key='-BEGIN-',disabled=False),
                   sg.B("<", key='-BACK-',disabled=False),
                   sg.T(text=page, key='-PAGE-', size=(2, 1)),
                   sg.B(">", key='-NEXT-',disabled=False),
                   sg.B(">>", key='-END-',disabled=False)
                   ]]
    
    create = [[sg.B('Create Team',key='-CREATE-',font=g.FONT,button_color=('white','darkblue')),
                   sg.T(' ',font=g.FONT,size=(12, 1))]]
    
    layout += [[sg.Col(create, element_justification='left'),sg.Col(displaylines, element_justification='left'),sg.Col(teamqtt, element_justification='center'),sg.Col(pagination, justification='right')]]
    layout += [[sg.B('Return')]]
    
               
    window = MyWindow(titlewindows, layout,keep_on_top=True, element_justification = 'center',finalize=True)
    window.my_move_to_center()

    if project == None:
        titlewindows='List of Members for all teams'
    else:
        titlewindows='List of Members for the team: '+team[3]+' of project: '+team[1]
        

    if g.DEBUG_OL >= 2:
        print('start',start,'end',end,'len(teamstotal)',len(teamstotal),'len(teamstotal)-linespage',len(teamstotal)-linespage)
    if end >= len(teamstotal):
        window['-END-'].update(disabled=True)
        window['-NEXT-'].update(disabled=True)
    if start  < linespage:
        window['-BEGIN-'].update(disabled=True)
        window['-BACK-'].update(disabled=True)

    
    while True:
        event1, values1 = window.read()
        if g.DEBUG_OL >= 2:
            print(event1,values1)
                                                                                                          
        if event1 == sg.WIN_CLOSED or event1 == 'Return':
            window.close()
            return(None)
            exit()


        if event1 == '-PFILTER-':
            order1=1
            order2=3
            order3=4
            page = 1
            window.close()
            list_teams_gui(project,page,linespage,order1, order2, order3,info)
            
            
        if event1 == '-TFILTER-':
            order1=3
            order2=1
            order3=4
            page = 1
            window.close()
            list_teams_gui(project,page,linespage,order1, order2, order3,info)
 
        if event1 == '-LFILTER-':
            order1=6
            order2=1
            order3=3
            page = 1
            window.close()
            list_teams_gui(project,page,linespage,order1, order2, order3,info)

        if event1 == "-DLINES-":
            if g.DEBUG_OL >= 2:
                print('type',type(values1['-DLINES-']),'value',values1['-DLINES-'],values1['-DLINES-'].isnumeric())
            if values1['-DLINES-'].isnumeric()== True:
                linespage=int(values1['-DLINES-'])
                page=1
                window.close()
                list_teams_gui(project,page,linespage,order1, order2, order3,info)
 
        if event1 == '-PROJECT-':
            page=1
            window.close()
            project=values1['-PROJECT-']
            list_teams_gui(project,page,linespage,order1, order2, order3,info)
            
        if event1 == "-NEXT-":
            page += 1
            window.close()
            list_teams_gui(project,page,linespage,order1, order2, order3,info)

        if event1 == "-BACK-":
            page -= 1
            window.close()
            list_teams_gui(project,page,linespage,order1, order2, order3,info)
        
        if event1 == "-BEGIN-":
            page = 1
            window.close()
            list_teams_gui(project,page,linespage,order1, order2, order3,info)
        
        if event1 == "-END-":
            page = (items-linespage)//linespage+1
            print(page)
            window.close()
            list_teams_gui(project,page,linespage,order1, order2, order3,info)   
            
        if event1 == "-CREATE-":
            window.close()
            create_team_gui()
            page = 1
            list_teams_gui(project,page,linespage,order1, order2, order3,info)
            
        if '-PHOTOIMG-' in event1:
            a=int(event1.split("-")[-1])
            toto=Teams.objects(TeamID=a).first()

            teamlogo=toto.TeamLogo
            print(a,'-PHOTOIMG-'+str(a),teamlogo)

            photo_layout=[[#sg.T('Select image', font=g.FONT, size=(15,1)),
                           sg.I(key='-IMG-',enable_events=True,font=g.FONT, size=(25,1)),
                           sg.FileBrowse(file_types=(('All files',['*.jpeg','*.jpg','*.png']),("JPEG Files","*.jpeg"),("JPG Files","*.jpg"),("PNG Files","*.png")))],
                          [sg.Image(key='-NEWPHOTO-', data=convert_to_bytes(teamlogo,resize=(250,250)))]]
            
            layout = [[photo_layout],
            [sg.B('Update', enable_events=True), sg.Cancel()]]
 

#            window.Hide()
            window.close()
            window1 = MyWindow('Select new image', layout,finalize=True)
            window1.my_move_to_center()
   
            while True:
                event2, values2 = window1.read()
                if g.DEBUG_OL >= 1:
                    print(event2,values2)
                                                                                                          
                if event2 == sg.WIN_CLOSED or event2 == 'Cancel':
                    window1.close()
                    break
                    
                if '-IMG-' in event2:
                    teamlogo=values2['-IMG-']
                    print(values2['-IMG-'])
                    window1['-NEWPHOTO-'].update(data=convert_to_bytes(values2['-IMG-'],resize=(250,250)))
                
                if event2 == 'Update':
                    update_team_logo(a,teamlogo)
                    break
            
            window1.close()        
            list_teams_gui(project,page,linespage,order1, order2, order3,info)
            
             
        if '-ARCH-' in event1:
            a=int(event1.split("-")[-1])
            itemstatus=Teams.objects(TeamID=a).first()
            if g.DEBUG_OL >= 1:
                print(itemstatus.Archived)
            if itemstatus.Archived == False:
                newstatus=True
            else:
                newstatus=False
                
            if g.DEBUG_OL >= 1:
                print(a,newstatus)
            archive_team(a,newstatus)
            page = 1
            window.close()
            list_teams_gui(project,page,linespage,order1, order2, order3,info)

        if '-UPDT-' in event1:
            a=int(event1.split("-")[-1])
            itemupd=Teams.objects(TeamID=a).first()
            projid='-PID-'+str(a)
            team='-TNAME-'+str(a)
            desc='-TDESC-'+str(a)
            photo='-PHOTO-'+str(a)
            
            if g.DEBUG_OL >= 1:
                print(a,values1[projid],values1[team],values1[desc],values1[photo])
                
            update_team(values1[projid],a,values1[team],values1[desc],values1[photo])
            page = 1
            window.close()
            list_teams_gui(project,page,linespage,order1, order2, order3,info)
            


# In[9]:


#list_teams_gui()


# ## Select teams by Project

# In[ ]:


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

