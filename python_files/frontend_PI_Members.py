#!/usr/bin/env python
# coding: utf-8

# ## frontend_PI_Members

# In[1]:


import os
import time
import bcrypt
from datetime import datetime
import PySimpleGUI as sg
from operator import itemgetter
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


# In[3]:


connect('PIPlanning')


# ## create_member_gui(info)

# In[ ]:


def create_member_gui(info='Info'):
    if g.DEBUG_OL >= 1:
        print('--- function: create_member_gui(',info,')')
 
    sg.set_options(element_padding=(5, 10))
    fin=0
    
    projects_list=list_projects()
    comboproj = []
    for project in projects_list:
        if g.DEBUG_OL >= 2:
            print(project.Archived)
        if project.Archived == False:
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
    
    
    info_layout = [sg.T(info,font=g.FONT,justification="left")]
 
    left_layout = [
        [sg.T('Project Selection', size=(20, 1),font=g.FONT), sg.Combo(comboproj,key='-PROJ-',enable_events=True,size=(20, 1),font=g.FONT)],
        [sg.T('Team Name', size=(20, 1),key='-TXTTEAM-',font=g.FONT,visible=False), sg.Combo(team,key='-TEAM-',enable_events=True,visible=False,size=(20, 1),font=g.FONT)],
    ]
    
    bottom_layout=[[sg.T('Last Name',key='-L1-',size=(15,1),font=g.FONT,visible=True),sg.I("",key='-MNAME-',visible=True,size=(20,1)),
                    sg.T('First Name',key='-F1-',size=(15,1),font=g.FONT,visible=True),sg.I("",key='-FNAME-',visible=True,size=(20,1))],
                   [sg.T('Alias',key='-A1-',size=(15,1),font=g.FONT,visible=True),sg.I("",key='-ALIAS-',visible=True,size=(20,1))],
                   [sg.T('Email',key='-E1-',size=(15,1),font=g.FONT,visible=True),sg.I("",key='-EMAIL-',visible=True,size=(20,1))],
                   [sg.T('Role', size=(15, 1),font=g.FONT), sg.Combo(comboroles,key='-ROLE-',enable_events=True,size=(20, 1),font=g.FONT)],
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
            fin=0
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
                    print(i[3],i[7])
                if i[7] == False:
                    teams.append(i[3])
            window['-TXTTEAM-'].update(visible=True)
            window['-TEAM-'].update(values=teams,visible=True)
            

              
        elif '-TEAM-' in event:
            team=values['-TEAM-']
            if g.DEBUG_OL >= 2:
                print(team)


            window['-MEMBER-'].update(visible=True)

        elif event == 'Add':
            
            if values['-MNAME-'] == "" or values['-FNAME-'] == "" or values['-ALIAS-'] == "" or values['-EMAIL-'] == "" or values['-ROLE-'] == "":
                sg.popup('Please fill all fields!',title="error",auto_close=True, auto_close_duration=2,)
                window.close()
                fin=1
                break
            if values['-EMAIL-'].find('@') == -1:
                sg.popup('Please fill the email correctly!',title="error",auto_close=True, auto_close_duration=2,)
                window.close()
                fin=1
                break
                
                
            teamselected=Teams.objects(Archived=False,TeamName=values['-TEAM-']).first()
            roleselected=Roles.objects(Archived=False,RoleName=values['-ROLE-']).first()
            teamid=teamselected.TeamID
            roleid=roleselected.RoleID
            username=values['-MNAME-'].capitalize()
            firstname=values['-FNAME-'].capitalize()
            alias=values['-ALIAS-'].lower()
            email=values['-EMAIL-'].lower()

            if g.DEBUG_OL >= 2:
                print('event:',event,'\nvalues:',values)
#                print('name:',values['-MNAME-'],'first name:',values['-FNAME-'],'alias:',values['-ALIAS-'],'email:',values['-EMAIL-'],'teamid:',teamid,'roleid:',roleid)
                print('name:',username,'first name:',firstname,'alias:',alias,'email:',email,'teamid:',teamid,'roleid:',roleid)

            id=create_member(username,firstname,alias,email,teamid,roleid)
            if g.DEBUG_OL >= 2:
                print('New user created with id:',id)
            sg.popup('New user '+alias+' created with id: '+str(id),title="info",auto_close=True, auto_close_duration=3,)
            window.close()
            
    if fin == 1:
        create_member_gui()


# In[ ]:


#create_member_gui()


# ## list_members_gui(teamid,page,linespage,info='info')

# In[120]:


def list_members_gui(teamid=None,page=1,linespage=5,order1=8,order2=1,order3=3,info='info'):
    if g.DEBUG_OL >= 1:
        print('--- function: list_members_gui(',teamid,page,linespage,order1, order2, order3,info,')')
 
    #    global page
    members=[]
    memberstotal=[]
    members1=[]
    comboteams=[]
    comboroles=[]
    
    if teamid == None:
        members1=list_members_by_team()
        teams=list_teams()
    else:
        members1=list_members_by_team(teamid)
        teamsearch=Teams.objects(TeamID=members1[0][12]).first()
        teams=list_teams(teamsearch.ProjectID)
        
    for i in teams:
        if i[7] == False:
            comboteams.append(i[3])
            
    roles=Roles.objects(Archived=False)
    for i in roles:
        comboroles.append(i.RoleName)
    
    comboteams.sort()
    comboroles.sort()
    
    if g.DEBUG_OL >= 2:
        print(teams[0][1],comboteams,comboroles)

#return [memberid,name,alias,firstname,email,theme,admin,status,lastupdate,firstcon,projectid,project,teamid,team,roleid,role]
#   members = sorted(members1, key=lambda x: (x[8], x[2]))
    order1=int(order1)
    order2=int(order2)
    order3=int(order3)

    memberstotal=sorted(members1, key = itemgetter(order1, order2,order3))

    items=len(memberstotal)

    start=page*linespage-linespage
    end=start+linespage
    if end > items:
        end = items
    a=0
    b=0
 
    if g.DEBUG_OL >=2:
        print('items:',items,'\tstart:',start,'\tend:',end)
    
    dteams={}
    for i in range(start,end):
        members.append(memberstotal[i])
        if g.DEBUG_OL >= 2:
            print(members[a])
        a=+1
    
    if teamid == None:
        titlewindows='List of Members for all teams'
    else:
        titlewindows='List of Members for the team: '+members[0][13]+' of project: '+members[0][11]
        
    sg.set_options(element_padding=(5, 5))
#    list_teams=list_teams_all()
    layout = [[sg.T(info,font=g.FONT,justification="left")],
              [sg.T('Team Name',font=g.FONT,key='-TFILTER-',enable_events=True, size=(20, 1)),
               sg.T('Member Name',font=g.FONT,key='-NFILTER-',enable_events=True, size=(20, 1)),
               sg.T('Member Firstname',font=g.FONT,size=(20, 1)),
               sg.T('Member Alias',font=g.FONT,key='-AFILTER-',enable_events=True, size=(20, 1)),
               sg.T('Member Email',font=g.FONT,key='-MFILTER-',enable_events=True, size=(20, 1)),
               sg.T('Member Role',font=g.FONT,key='-RFILTER-',enable_events=True, size=(20, 1)),
               sg.T('Last Update',font=g.FONT,key='-LFILTER-',enable_events=True, size=(10, 1)),
               sg.T(' ',font=g.FONT,size=(5, 1)),
               sg.T('Change Status',font=g.FONT,size=(10, 1))
              ],
              [sg.Combo(comboteams,key='-TEAMS-',enable_events=True,size=(20, 1),font=g.FONT),sg.T(" ",size=(144, 1),font=g.FONT)]
             ]
    idx=0
    for member in members:
        if g.DEBUG_OL >= 2:
            print('MemberID',member[0],'\tProjectID',member[10],'\Status:',member[7])
        
        if member[7] is False:
            status='Active'
            FONT1=g.FONT
            bfcolor='white'
            bbcolor='green'
            
        else:
            status='Archived'
            FONT1=g.FONT+' italic'
            bfcolor='white'
            bbcolor='firebrick3'

   
        row = [
#            sg.I(member[13],enable_events=True,key=f'-TNAME-{member[0]}', font=g.FONT, size=(20,1)),
               sg.Combo(comboteams,enable_events=True,key=f'-TNAME-{member[0]}',default_value=member[13],size=(20, 1),font=g.FONT),
               sg.I(member[12],enable_events=False, visible=False,key=f'-TID-{member[0]}', font=g.FONT, size=(20,1)),
               sg.I(member[1],enable_events=True,key=f'-NAME-{member[0]}', font=g.FONT, size=(20,1)),
               sg.I(member[3],enable_events=True,key=f'-FNAME-{member[0]}', font=g.FONT,size=(20,1)),
               sg.I(member[2],enable_events=True,key=f'-ALIAS-{member[0]}', font=g.FONT,size=(20,1)),
               sg.I(member[4],enable_events=True,key=f'-EMAIL-{member[0]}', font=g.FONT,size=(20,1)),
               sg.Combo(comboroles,enable_events=True,key=f'-ROLE-{member[0]}',default_value=member[15],font=g.FONT,size=(20,1)),
               sg.I(member[14],enable_events=False, visible=False,key=f'-ROLEID-{member[0]}', font=g.FONT,size=(20,1)),
               
               sg.B('Update',enable_events=True, key=f'-UPDT-{member[0]}',font=g.FONT,button_color=('white','darkblue'),size=(10,1)),
               sg.T(' ',font=g.FONT,size=(5, 1)),
               sg.B(status, enable_events=True,key=f'-ARCH-{member[0]}',font=FONT1,button_color=(bfcolor,bbcolor),size=(10,1)),
             ]
        layout.append(row)
        idx+=1
   
    
    memberqtt= [[sg.T('Total members found: ',font=g.FONT, size=(24, 1)),sg.I(items,key='-MFOUND-',enable_events=False,disabled=True,visible=True,size=(10,1))]
                  ]
    
    displaylines= [[sg.T('Displayed Lines:',font=g.FONT, size=(22, 1)),sg.I(linespage,key='-DLINES-',enable_events=True,visible=True,size=(10,1))]
                  ]
    
    pagination = [[sg.B('<<', key='-BEGIN-',disabled=False),
                   sg.B("<", key='-BACK-',disabled=False),
                   sg.T(text=page, key='-PAGE-', size=(2, 1)),
                   sg.B(">", key='-NEXT-',disabled=False),
                   sg.B(">>", key='-END-',disabled=False)
                   ]]
    
    createmember = [[sg.B('Create Member',key='-CMEMBER-',font=g.FONT,button_color=('white','darkblue')),
                   sg.T(' ',font=g.FONT,size=(12, 1))]]
    
    
 
    layout += [[sg.Col(createmember, element_justification='left'),sg.Col(displaylines, element_justification='left'),sg.Col(memberqtt, element_justification='center'),sg.Col(pagination, justification='right')]]
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
            fin=0
            break
                                                                                                          

        if event1 == '-TFILTER-':
            order1=8
            order2=1
            order3=3
            page = 1
            window.close()
            list_members_gui(teamid,page,linespage,order1, order2, order3,info)
            
            
        if event1 == '-AFILTER-':
            order1=2
            order2=1
            order3=3
            page = 1
            window.close()
            list_members_gui(teamid,page,linespage,order1, order2, order3,info)
 
        if event1 == '-NFILTER-':
            order1=1
            order2=3
            order3=8
            page = 1
            window.close()
            list_members_gui(teamid,page,linespage,order1, order2, order3,info)

        if event1 == '-RFILTER-':
            order1=10
            order2=1
            order3=3
            page = 1
            window.close()
            list_members_gui(teamid,page,linespage,order1, order2, order3,info)

        if event1 == '-LFILTER-':
            order1=4
            order2=1
            order3=3
            page = 1
            window.close()
            list_members_gui(teamid,page,linespage,order1, order2, order3,info)


        if event1 == "-DLINES-":
            if g.DEBUG_OL >= 2:
                print('type',type(values1['-DLINES-']),'value',values1['-DLINES-'],values1['-DLINES-'].isnumeric())
            if values1['-DLINES-'].isnumeric()== True:
                linespage=int(values1['-DLINES-'])
                page=1
                window.close()
                list_members_gui(teamid,page,linespage,order1, order2, order3,info)
                                                  
        if event1 == "-NEXT-":
            page += 1
            window.close()
            list_members_gui(teamid,page,linespage,order1, order2, order3,info)

        if event1 == "-BACK-":
            page -= 1
            window.close()
            list_members_gui(teamid,page,linespage,order1, order2, order3,info)
        
        if event1 == "-BEGIN-":
            page = 1
            window.close()
            list_members_gui(teamid,page,linespage,order1, order2, order3,info)
        
        if event1 == "-END-":
            page = (items-linespage)//linespage+1
            print(page)
            window.close()
            list_members_gui(teamid,page,linespage,order1, order2, order3,info)

        if event1 == "-CMEMBER-":
            window.close()
            create_member_gui()
            page = 1
            list_members_gui(teamid,page,linespage,order1, order2, order3,info)
            
            
        if event1 == '-TEAMS-':
            page=1
            window.close()
            newteam=Teams.objects(TeamName=values1['-TEAMS-']).first()
            teamid=newteam.TeamID
            list_members_gui(teamid,page,linespage,order1, order2, order3,info)
             

        if '-ARCH-' in event1:
            a=int(event1.split("-")[-1])
            itemstatus=Members.objects(MemberID=a).first()
            if g.DEBUG_OL >= 2:
                print(itemstatus.Archived)
            if itemstatus.Archived == False:
                newstatus=True
            else:
                newstatus=False
                
            if g.DEBUG_OL >= 2:
                print(a,newstatus)
            archive_member(a,newstatus)
            page = 1
            window.close()
            list_members_gui(teamid,page,linespage,order1, order2, order3,info)

        
        if '-TNAME-' in event1:
            a=int(event1.split("-")[-1])
            newname=values1[event1]
            if g.DEBUG_OL >= 2:
                print(a,newname,'\t',event1,values1)
            teamupd=Teams.objects(TeamName=newname).first()
            itemid='-TID-'+str(a)
            window[itemid].update(teamupd.TeamID)
            
            if g.DEBUG_OL >= 2:
                print(a,newname,'\t',event1,values1)
            

        if '-ROLE-' in event1:
            a=int(event1.split("-")[-1])
            newname=values1[event1]
            if g.DEBUG_OL >= 2:
                print(event1,values1)
            roleupd=Roles.objects(RoleName=newname).first()
            itemid='-ROLEID-'+str(a)
            window[itemid].update(roleupd.RoleID)
            
            if g.DEBUG_OL >= 2:
                print(a,newname,'\t',event1,values1)
 
        
        if '-UPDT-' in event1:
            if g.DEBUG_OL >= 2:
                print(event1,values1)
  
            a=int(event1.split("-")[-1])
            itemupd=Members.objects(MemberID=a).first()
#            teamlinkupd=LinkMemberTeam.objects(MemberID=a).first())
            if g.DEBUG_OL >= 2:
                print(a,itemupd)
            oldteamid=teamid    
            teamid='-TID-'+str(itemupd.MemberID)
            name='-NAME-'+str(itemupd.MemberID)
            fname='-FNAME-'+str(itemupd.MemberID)
            alias='-ALIAS-'+str(itemupd.MemberID)
            email='-EMAIL-'+str(itemupd.MemberID)
            roleid='-ROLEID-'+str(itemupd.MemberID)
            
#            desc='-DESC-'+str(itemupd.RoleID)

            if g.DEBUG_OL >= 1:
                print(a,values1[teamid],values1[name],values1[fname],values1[alias],values1[email],values1[roleid])
            update_member(a,values1[teamid],values1[name],values1[fname],values1[alias],values1[email],values1[roleid])
            page = 1
            window.close()
            list_members_gui(oldteamid,page,linespage,order1, order2, order3,info)
       


# In[122]:


#list_members_gui('OKCorral')


# In[ ]:


print(os.getcwd(),__name__,'imported')


# In[ ]:




