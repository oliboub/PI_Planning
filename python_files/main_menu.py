#!/usr/bin/env python
# coding: utf-8

# # Main Menu for Safe PI Planning

# ## Imports

# In[1]:


import global_variables as g
g.init()
import PySimpleGUI as sg
from backend_PI import * # Import tout ce qui est spécifique au projet
from frontend_PI import *

connect('PIPlanning')

if g.DEBUG_OL >= 1:
    print("Debug mode active level :",g.DEBUG_OL)


# ## Documentation
# ### see doc_plantuml.jpynb

# -------
# ## Main

# In[2]:


def main(theme,projectid,project,admin=False):
    if g.DEBUG_OL >= 1:
        print('--- function main:(',theme,projectid,project,admin,')')
    menu_admin = [
        ['Parameters',
         ['Project', ['Create Project', 'List Project', 'Archive Project'],
         ['Teams',['Create Team','List Teams',['List All Teams','List Teams by Project'],'Archive Team'],
         ['Members',['Create member','List members','Archive member']]]]
        ],
         ['My Info',['Who am I','Select Theme']],
        ['Exit', ['Quit']]
    ]
    
    menu_std = [
        ['My Project', ['List project teams','List our team members','list teams members']],['Tasks',['Create task','List tasks']],
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
        if event == 'Create Project':
            info='Create new project'
            create_project_gui(info)
        if event == 'List Project':
            info='List of active projects'
            ActualProjectID,ActualProjectName, ActualProjectDesc=list_projects_gui(info)
            if g.DEBUG_OL >= 2:
                print('ActualProjectID:',ActualProjectID,'\tActualProjectName;',ActualProjectName,'\tActualProjectDesc:',ActualProjectDesc)
        if event == 'Archive Project':
            info='Archivage de projet non utilisé'
            ArchivedProjectName=archive_project_gui(info)
            if g.DEBUG_OL >= 2:
                print('ArchivedProjectName;',ArchivedProjectName)
        
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
            idx=list_members_gui(teamid,1,5,info='List of team members')
  

    #--- My Info
        if event == "Who am I":
            who_am_i_gui(UserAlias)
        
        if event == "Select Theme":
            theme1=select_theme_gui(memberid,theme)
            if g.DEBUG_OL >= 2:
                print(theme1)
            sg.theme(theme1)
            window.close()
            main(theme1,projectid)

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




