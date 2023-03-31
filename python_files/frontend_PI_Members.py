#!/usr/bin/env python
# coding: utf-8

# ## PI Members Management

# In[1]:


import PySimpleGUI as sg
from backend_PI import * # Import tout ce qui est spécifique au projet
import operator
import os

connect('PIPlanning')
if g.DEBUG_OL == -1:
    print("Debug mode active level :",g.DEBUG_OL)


# ## create_member_gui(info)

# In[ ]:


def create_member_gui(info='Info'):
    if g.DEBUG_OL >= 1:
        print('--- function: create_member_gui(',info,')')
 
    sg.set_options(element_padding=(5, 10))

    projects_list=list_projects()
    comboproj = []
    for project in projects_list:
        comboproj.append(project.ProjectName)
    if g.DEBUG_OL >= 2:
        print(comboproj)
    
    team=[]
    combomembers=[]
    comboroles=[]
    
    roles=Roles.objects(Archived=False)
    for i in roles:
        comboroles.append(i.RoleName)
    if g.DEBUG_OL >= 2:
        print(comboroles)
    
    
    info_layout = [sg.T(info,font='Calibri 11',justification="left")]
 
    left_layout = [
        [sg.T('Project Selection', size=(20, 1),font='Calibri 11'), sg.Combo(comboproj,key='-PROJ-',enable_events=True,size=(20, 1),font='Calibri 11')],
        [sg.T('Team Name', size=(20, 1),key='-TXTTEAM-',font='Calibri 11',visible=False), sg.Combo(team,key='-TEAM-',enable_events=True,visible=False,size=(20, 1),font='Calibri 11')],
    ]
    
    bottom_layout=[[sg.T('Last Name',key='-L1-',size=(15,1),font='Calibri 11',visible=True),sg.I("",key='-MNAME-',visible=True,size=(20,1)),
                    sg.T('First Name',key='-F1-',size=(15,1),font='Calibri 11',visible=True),sg.I("",key='-FNAME-',visible=True,size=(20,1))],
                   [sg.T('Alias',key='-A1-',size=(15,1),font='Calibri 11',visible=True),sg.I("",key='-ALIAS-',visible=True,size=(20,1))],
                   [sg.T('Email',key='-E1-',size=(15,1),font='Calibri 11',visible=True),sg.I("",key='-EMAIL-',visible=True,size=(20,1))],
                   [sg.T('Role', size=(15, 1),font='Calibri 11'), sg.Combo(comboroles,key='-ROLE-',enable_events=True,size=(20, 1),font='Calibri 11')],
                  ]
    
#    layout = [info_layout,[sg.Frame("Select perimeter", left_layout, vertical_alignment='top', pad=((10, 10), (10, 10)))],
#            [sg.B('Add', enable_events=True), sg.Cancel()]]
             
    layout = [info_layout,[sg.Frame("Select perimeter", left_layout, vertical_alignment='top', pad=((10, 10), (10, 10)))],
              [sg.Frame("New Member information", bottom_layout,key='-MEMBER-', vertical_alignment='top',pad=((10, 10), (10, 10)),visible=False)],
              [sg.B('Add', enable_events=True), sg.Cancel()]]
        
    window = MyWindow('Create member', layout,finalize=True)
    window.my_move_to_center()
    
    while True:
        event, values = window.read()
#        print(event,values)
        
        if event == sg.WIN_CLOSED or event == 'Cancel':
#            print(event)
            window.close()
            break
 
        elif '-PROJ-' in event:
            window['-MEMBER-'].update(visible=False)
            if g.DEBUG_OL >= 2:
                print(values['-PROJ-'])
            project=values['-PROJ-']
            teams_list = []
            teams_list=list_teams(project)
            teams=[]
            for i in teams_list:
                if g.DEBUG_OL >= 2:
                    print(i[1])
                teams.append(i[1])
            window['-TXTTEAM-'].update(visible=True)
            window['-TEAM-'].update(values=teams,visible=True)
            

              
        elif '-TEAM-' in event:
            team=values['-TEAM-']
            if g.DEBUG_OL >= 2:
                print(team)


            members=query_members_by_team(team)
            for i in members:
                if g.DEBUG_OL >= 2:
                    print(i[2])
                combomembers.append(i[2])
            print(combomembers)
            
            titre='Member information for : '+project+' and team:'+team
            
            window['-MEMBER-'].update(visible=True)

        elif event == 'Add':
            teamselected=Teams.objects(Archived=False,TeamName=values['-TEAM-']).first()
            roleselected=Roles.objects(Archived=False,RoleName=values['-ROLE-']).first()
            teamid=teamselected.TeamID
            roleid=roleselected.RoleID

            if g.DEBUG_OL >= 2:
                print('event:',event,'\nvalues:',values)
                print('name:',values['-MNAME-'],'first name:',values['-FNAME-'],'alias:',values['-ALIAS-'],'email:',values['-EMAIL-'],'teamid:',teamid,'roleid:',roleid)
            id=create_member(values['-MNAME-'],values['-FNAME-'],values['-ALIAS-'],values['-EMAIL-'],teamid,roleid)
            if g.DEBUG_OL >= 2:
                print('New user created with id:',id)
            sg.popup('New user '+values['-ALIAS-']+' created with id: '+str(id),title="info",auto_close=True, auto_close_duration=3,)
            window.close()


# In[ ]:


#create_member_gui()


# ## list_members_gui(teamid,page,linespage,info='info')
# **WIP**

# In[9]:


def list_members_gui(teamid,page,linespage=5,info='info'):
    if g.DEBUG_OL >= 1:
        print('--- function: list_members_gui(',teamid,page,linespage,info,')')
 
    #    global page
    members=[]
    memberstotal=[]
    members1=query_members_by_team(teamid)
 #   members = sorted(members1, key=lambda x: (x[8], x[2]))
    memberstotal=sorted(members1, key = operator.itemgetter(6, 1, 3))

    items=len(memberstotal)

    start=page*linespage-linespage
    end=start+linespage
    if end > items:
        end = items
    a=0
 
    if g.DEBUG_OL >=2:
        print('items:',items,'\tstart:',start,'\tend:',end)
    

    for i in range(start,end):
        members.append(memberstotal[i])
        if g.DEBUG_OL >= 2:
            print(members[a])
        a=+1
    
    if teamid == 'All':
        titlewindows='List of Members for all teams'
    else:
        titlewindows='List of Members for the team: '+members[0][6]
        
    sg.set_options(element_padding=(5, 5))
#    list_teams=list_teams_all()
    layout = [[sg.T(info,font='Calibri 11',justification="left")],
              [sg.T('Team Name',font='Calibri 11', size=(20, 1)),
               sg.T('Member Name',font='Calibri 11', size=(20, 1)),
               sg.T('Member Firstname',font='Calibri 11',size=(20, 1)),
               sg.T('Member Alias',font='Calibri 11', size=(20, 1)),
               sg.T('Member Role',font='Calibri 11', size=(20, 1)),
               sg.T('Member Email',font='Calibri 11', size=(20, 1)),
              ]]
    idx=0
    for member in members:
        if g.DEBUG_OL >= 2:
            print('MemberID',member[0],'\tProjectID',member[6],'\tTeam:',member[7])

        row = [sg.I(member[6],disabled=True, font='Calibri 11', size=(20,1)),
               sg.I(member[1],disabled=True, font='Calibri 11', size=(20,1)),
               sg.I(member[3],disabled=True, font='Calibri 11',size=(20,1)),
               sg.I(member[2],disabled=True, font='Calibri 11',size=(20,1)),
               sg.I(member[8],disabled=True, font='Calibri 11',size=(20,1)),
               sg.I(member[4],disabled=True, font='Calibri 11',size=(20,1)),
              ]
        layout.append(row)
        idx+=1
   
    
    memberqtt= [[sg.T('Total members found: ',font='Calibri 11', size=(24, 1)),sg.I(items,key='-MFOUND-',enable_events=False,disabled=True,visible=True,size=(10,1))]
                  ]
    
    displaylines= [[sg.T('Displayed Lines:',font='Calibri 11', size=(22, 1)),sg.I(linespage,key='-DLINES-',enable_events=True,visible=True,size=(10,1))]
                  ]
    
    pagination = [[sg.B('<<', key='-BEGIN-',disabled=False),
                   sg.B("<", key='-BACK-',disabled=False),
                   sg.T(text=page, key='-PAGE-', size=(2, 1)),
                   sg.B(">", key='-NEXT-',disabled=False),
                   sg.B(">>", key='-END-',disabled=False)
                   ]]
    layout += [[sg.Col(displaylines, element_justification='left'),sg.Col(memberqtt, element_justification='center'),sg.Col(pagination, justification='right')]]
    layout += [[sg.B('Return')]]
    
               
    window = MyWindow(titlewindows, layout,keep_on_top=True, element_justification = 'center',finalize=True)
    window.my_move_to_center()

    if g.DEBUG_OL >= 2:
        print('start',start,'end',end,'len(memberstotal)',len(memberstotal),'len(memberstotal)-linespage',len(memberstotal)-linespage)
    if end >= len(memberstotal):
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
            break
                                                                                                          
        if event1 == "-DLINES-":
            if g.DEBUG_OL >= 2:
                print('type',type(values1['-DLINES-']),'value',values1['-DLINES-'],values1['-DLINES-'].isnumeric())
            if values1['-DLINES-'].isnumeric()== True:
                linespage=int(values1['-DLINES-'])
                window.close()
                list_members_gui(teamid,page,linespage,info)
                                                  
        if event1 == "-NEXT-":
            page += 1
            window.close()
            list_members_gui(teamid,page,linespage,info)

        if event1 == "-BACK-":
            page -= 1
            window.close()
            list_members_gui(teamid,page,linespage,info)
        
        if event1 == "-BEGIN-":
            page = 1
            window.close()
            list_members_gui(teamid,page,linespage,info)
        
        if event1 == "-END-":
            page = (items-linespage)//linespage+1
            print(page)
            window.close()
            list_members_gui(teamid,page,linespage,info)


# In[10]:


#list_members_gui( 1, 1, 3, "List of team members")


# In[ ]:


print(os.getcwd(),__name__,'imported')


# In[ ]:




