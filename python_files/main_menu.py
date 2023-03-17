#!/usr/bin/env python
# coding: utf-8

# # Main Menu for PI PLanning

# ## Imports

# In[3]:


import PySimpleGUI as sg
from backend_PI import * # Import tout ce qui est spécifique au projet
from frontend_PI import *

connect('PIPlanning')


# ## Documentation
# ### see doc_plantuml.jpynb

# -------
# ## Main

# In[27]:


def main(theme,admin=False):
    print('function main:(',theme,admin,')')
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
        ['My Project', ['List my team','List our members']],['Tasks',['Create task','List tasks']],
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
            print('ActualProjectID:',ActualProjectID,'\tActualProjectName;',ActualProjectName,'\tActualProjectDesc:',ActualProjectDesc)
        if event == 'Archive Project':
            info='Archivage de projet non utilisé'
            ArchivedProjectName=archive_project_gui(info)
            print('ArchivedProjectName;',ArchivedProjectName)
        
#--- Teams
        if event == 'Create Team':
            info='Créer votre nouvelle equipe'
            create_team_gui(info)

        if event == "List All Teams":
            info='List of All active Teams even if non allocated to project'
            teams=list_teams_page(1)
            print(teams)
            list_all_teams_gui(1,teams,info)

        if event == "List Teams by Project":
            info='Select project top display associated teams'
            projectid=None
            projectid,projectname=select_project_gui() # a lan cer pour chercher les equipes d'un projet

            print(__name__,projectid,projectname)
            teams=list_teams_page(1,projectid)
            for a in teams.items:
                print(a.TeamName,'\t',a.TeamDescription,'\t',a.TeamLogo,'\t',a.ProjectID)
            info='Liste de toutes les equipes du projet '+ projectname
            list_all_teams_gui(1,teams,info)

        if event == "List my team":
            info='info'
            print(__name__,projectid,projectname)
            teams=list_teams_page(1,projectid)
            for a in teams.items:
                print(a.TeamName,'\t',a.TeamDescription,'\t',a.TeamLogo,'\t',a.ProjectID)
            info='Liste de toutes les equipes du projet '+ projectname
            list_all_teams_gui(1,teams,info)
 
#--- My Info
        if event == "Who am I":
            who_am_i_gui(UserAlias)
        
        if event == "Select Theme":
            theme1=select_theme_gui(memberid,theme,)
            print(theme1)
            sg.theme(theme1)
            window.close()
            main(theme1)

if __name__ == '__main__':
    theme='LightBlue2'
    global font
    font='Calibri 11'
    page = 1
#    UserAlias=user_alias_gui()
    UserAlias=login_window()
    print(UserAlias)
    
    if UserAlias != 'None':
        memberid,name,firstname,email,theme,project,projectid,team,role,admin,firstcon=query_member_alias(UserAlias)
        sg.theme(theme)
        main(theme,admin)
    else:
        toto="Bye"
        sg.popup(toto,title="info",auto_close=True, auto_close_duration=2,)


# In[ ]:




