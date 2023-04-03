#!/usr/bin/env python
# coding: utf-8

# # Main Menu for Safe PI Planning

# ## Imports

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
from frontend_PI_Members import *
from frontend_PI_Users import *
from frontend_PI_Projects import *
from frontend_PI_Teams import *
from frontend_PI_Tasks import *
from frontend_PI_Roles import *
time.sleep(1)


# In[ ]:


connect('PIPlanning')


# In[ ]:


if g.DEBUG_OL >= 1:
    print("Debug mode active level :",g.DEBUG_OL)


# ## Documentation
# ### see doc_plantuml.jpynb

# -------
# ## Main

# In[ ]:


def main(theme,projectid,project,admin=False):
    if g.DEBUG_OL >= 1:
        print('--- function main:(',theme,projectid,project,admin,')')
    menu_admin = [
        ['Management',
         ['Manage Projects',
         'Manage Teams',
         'Manage Members',
         'Manage Roles'],
        ],
         ['My Info',['Who am I','Select Theme']],
        ['Exit', ['Quit']]
    ]
        
    
    menu_std = [
        ['My Project', ['List project teams','List project members','---','List our team members']],['Tasks',['Create task','List tasks']],
        ['My Info',['Who am I','Select Theme']],
        ['Exit', ['Quit']]
    ]
   
    if admin == True:
        layout = [[sg.Menu(menu_admin)],
              [sg.Image(data=convert_to_bytes('../imagesDB/safe.png', resize=(490, 220)))]] 
    else:
        layout = [[sg.Menu(menu_std)],
              [sg.Image(data=convert_to_bytes('../imagesDB/safe.png', resize=(490, 220)))]] 
    
    #background_color='#6c69df'
    window = MyWindow('PI PLanning',layout,icon='../imagesDB/agile.ico',finalize=True)
    window.my_move_to_center()
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Quit':
            window.close()
            break

#--- Projects
        if event == 'Manage Projects':
            info='List of active projects'
            list_projects_gui(1,5,info)
        
#--- Teams
        if event == 'Create Team':
            info='Créer votre nouvelle equipe'
            create_team_gui(info)

        if event == "List All Teams":
            info='List of All active Teams even if non allocated to project'
            teams=list_teams_page(1)
            if g.DEBUG_OL >= 2:
                print(teams)
            list_all_teams_gui(1,teams,info)

        if event == "List Teams by Project":
            info='Select project top display associated teams'
            projectid=None
            projectid,projectname=select_project_gui() # a lancer pour chercher les equipes d'un projet
            teams=list_teams_page(1,projectid)

            if g.DEBUG_OL >= 2:
                print(__name__,projectid,projectname)
                for a in teams.items:
                    print(a.TeamName,'\t',a.TeamDescription,'\t',a.TeamLogo,'\t',a.ProjectID)
            info='Liste de toutes les equipes du projet '+ projectname
            list_all_teams_gui(1,teams,info)
            
        if event == "Archive Team":
            if g.DEBUG_OL >= 2:
                print(__name__,projectid,projectname) 
            teams=list_teams_page(1)
                    

        if event == "List project teams":
            if g.DEBUG_OL >= 2:
                print(__name__,projectid,project)
            teams=list_teams_page(1,projectid)
            if g.DEBUG_OL >= 2:
                for a in teams.items:
                    print(a.TeamName,'\t',a.TeamDescription,'\t',a.TeamLogo,'\t',a.ProjectID)
            info='Lists of teams for your project: '+project
            list_all_teams_gui(1,teams,info)
 

        if event == 'Create member':
            if g.DEBUG_OL >= 2:
                print(__name__)
            idx=create_member_gui('Create a new member allocated to a project and a team')
 
        if event == 'List our team members':
            if g.DEBUG_OL >= 2:
                print(__name__)
            idx=list_members_gui(teamid,1,5,8,1,3,info='List of team members')
 
        if event == 'List project members':
            if g.DEBUG_OL >= 2:
                print(__name__)
            idx=list_members_gui('All',1,5,8,1,3,info='List of project members')
 

        if event == 'Manage Roles':
            if g.DEBUG_OL >= 2:
                print(__name__)
            idx=list_roles_gui(1,5,'List of all existing roles')

    #--- My Info
        if event == "Who am I":
            who_am_i_gui(UserAlias)
        
        if event == "Select Theme":
            theme1=select_theme_gui(memberid,theme)
            if g.DEBUG_OL >= 2:
                print(theme1)
            sg.theme(theme1)
            window.close()
            main(theme1,projectid,project,admin)

if __name__ == '__main__':
    
    theme=g.THEME
    
    page = 1

    #    UserAlias=user_alias_gui()
    UserAlias=login_window()
    if g.DEBUG_OL >= 2:
        print(UserAlias)
    
    if UserAlias != 'None':
        memberid,name,alias,firstname,email,theme,project,projectid,team,teamid,role,admin,firstcon=query_member_alias(UserAlias)
        sg.theme(theme)
        main(theme,projectid,project,admin)
    else:
        toto="Bye"
        sg.popup(toto,title="info",auto_close=True, auto_close_duration=2,)


# In[ ]:




