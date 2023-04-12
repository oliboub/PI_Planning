#!/usr/bin/env python
# coding: utf-8

# # Main Menu for Safe PI Planning

# ## Imports

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
from frontend_PI_Members import *
from frontend_PI_Users import *
from frontend_PI_Projects import *
from frontend_PI_Teams import *
from frontend_PI_Tasks import *
from frontend_PI_Roles import *
time.sleep(1)


# In[3]:


connect('PIPlanning')


# In[4]:


if g.DEBUG_OL >= 1:
    print("Debug mode active level :",g.DEBUG_OL)


# ## Documentation
# ### see doc_plantuml.jpynb

# -------
# ## Main

# In[5]:


def main(memberid,name,alias,firstname,email,theme,admin,portfolio,status,lastupdate,firstcon,projectid,project,teamid,team,roleid,role):
    if g.DEBUG_OL >= 1:
        print('--- function main:(',memberid,name,alias,firstname,email,theme,admin,portfolio,status,lastupdate,firstcon,projectid,project,teamid,team,roleid,role,')')
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
        ['My Project', ['List project teams','List project members','---','List our team members']],['Objectives'],['Tasks',['Create task','List tasks']],
        ['My Info',['Who am I','Select Theme']],
        ['Exit', ['Quit']]
    ]
    
    menu_portfolio = [
        [ 'Portfolio', ['Project management', 'Portfolio Management','Epic Management','PI Management' ]],
        ['My Info',['Who am I','Select Theme']],
        ['Exit', ['Quit']]
    ]
    
   
    if admin == True:
        layout = [[sg.Menu(menu_admin)],
              [sg.Image(data=convert_to_bytes('../imagesDB/safe.png', resize=(490, 220)))]] 

    elif portfolio == True:
        layout = [[sg.Menu(menu_portfolio)],
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

#--- Admin
        if event == 'Manage Projects':
            info='List of projects'
            list_projects_gui(memberid,1,5,info)
        
        if event == "Manage Teams":
            info='List of Teams'
            list_teams_gui(memberid,admin)

        if event == "Manage Members":
            info='List of Members'
            list_members_gui(memberid)

        if event == 'Manage Roles':
            if g.DEBUG_OL >= 2:
                print(__name__)
            idx=list_roles_gui(memberid,1,5,'List of all existing roles')


# standard user            
        if event == "List project teams":
            if g.DEBUG_OL >= 2:
                print(__name__,projectid,project)
            list_teams_gui(memberid,admin,projectid)
 

        if event == 'List our team members':
            info='List of or team members'
            if g.DEBUG_OL >= 2:
                print(__name__)
            list_members_gui(memberid,admin,teamid)
 
        if event == 'List project members':
            info='Lists of teams for your project: '+project
            if g.DEBUG_OL >= 2:
                print(__name__)
            idx=list_members_gui('All',1,5,8,1,3,info='List of project members')
 

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
        memberid,name,alias,firstname,email,theme,admin,portfolio,status,lastupdate,firstcon,projectid,project,teamid,team,roleid,role=query_member_alias(UserAlias)
        sg.theme(theme)
        main(memberid,name,alias,firstname,email,theme,admin,portfolio,status,lastupdate,firstcon,projectid,project,teamid,team,roleid,role)
    else:
        toto="Bye"
        sg.popup(toto,title="info",auto_close=True, auto_close_duration=2,)


# In[ ]:




