#!/usr/bin/env python
# coding: utf-8

# ## PI Roles Management

# In[ ]:


import global_variables as g
g.init()
import PySimpleGUI as sg
from backend_PI import * # Import tout ce qui est spécifique au projet
import operator
import os

connect('PIPlanning')
if g.DEBUG_OL == -1:
    print("Debug mode active level :",g.DEBUG_OL)


# ## create_role_gui(info)

# In[ ]:


def create_role_gui(info='Info'):
    if g.DEBUG_OL >= 1:
        print('--- function: create_role_gui(',info,')')
 
    sg.set_options(element_padding=(5, 10))

    existingroles=[]
    
    roles=Roles.objects(Archived=False)
    for i in roles:
        existingroles.append(i.RoleName.lower())
    if g.DEBUG_OL >= 2:
        print(existingroles)
    
    
    info_layout = [sg.T(info,font='Calibri 11',justification="left")]
 
    
    normal_layout=[[sg.T('Role',key='-R1-',size=(15,1),font=g.FONT,visible=True),sg.I("new role",key='-ROLE-',visible=True,font=g.FONT+' italic', size=(20,1))],
                   [sg.T('Role Description',key='-D1-',size=(15,1),font=g.FONT,visible=True),sg.I("Description",visible=True,key='-DESC-',font=g.FONT+' italic',size=(20,1))]
                  ]
    
          
    layout = [info_layout,[sg.Frame("Select perimeter", normal_layout, vertical_alignment='top', pad=((10, 10), (10, 10)))],
              [sg.B('Add', enable_events=True), sg.Cancel()]]
        
    window = MyWindow('Create role', layout,finalize=True)
    window.my_move_to_center()
    
    while True:
        event, values = window.read()
        if g.DEBUG_OL >= 2:
            print(event,values)
        
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            break
 

        elif event == 'Add':
            if g.DEBUG_OL >= 2:
                print('event:',event,'\nvalues:',values)
                print('Role:',values['-ROLE-'],'Description:',values['-DESC-'])
            if values['-ROLE-'].lower() in existingroles:
                sg.popup('role '+values['-ROLE-']+'  already exists !',title="info",auto_close=True, auto_close_duration=3,)
                window['-ROLE-'].update("new role")
            elif values['-DESC-'] == "Description":
                sg.popup('Please enter a description',title="info",auto_close=True, auto_close_duration=3,)
       
            else:
                id=create_role(values['-ROLE-'],values['-DESC-'])
                if g.DEBUG_OL >= 2:
                    print('New Role created with id:',id)
                sg.popup('New role '+values['-ROLE-']+' created with id: '+str(id),title="info",auto_close=True, auto_close_duration=3,)
                window.close()          
        


# In[ ]:


#create_role_gui('Please enter the new role to create')


# ## list_roles_gui(page,linespage,info='info')
# **WIP**

# In[ ]:


def list_roles_gui(page,linespage=5,info='info'):
    if g.DEBUG_OL >= 1:
        print('--- function: list_members_gui(',teamid,page,linespage,order1, order2, order3,info,')')
 
    #    global page
    members=[]
    memberstotal=[]
    members1=query_members_by_team(teamid)
 #   members = sorted(members1, key=lambda x: (x[8], x[2]))
    order1=int(order1)
    order2=int(order2)
    order3=int(order3)
    memberstotal=sorted(members1, key = operator.itemgetter(order1, order2, order3))

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
        titlewindows='List of Members for the team: '+members[0][8]+' of project: '+members[0][6]
        
    sg.set_options(element_padding=(5, 5))
#    list_teams=list_teams_all()
    layout = [[sg.T(info,font='Calibri 11',justification="left")],
              [sg.T('Team Name',font='Calibri 11',key='-TFILTER-',enable_events=True, size=(20, 1)),
               sg.T('Member Name',font='Calibri 11',key='-NFILTER-',enable_events=True, size=(20, 1)),
               sg.T('Member Firstname',font='Calibri 11',size=(20, 1)),
               sg.T('Member Alias',font='Calibri 11',key='-AFILTER-',enable_events=True, size=(20, 1)),
               sg.T('Member Role',font='Calibri 11',key='-RFILTER-',enable_events=True, size=(20, 1)),
               sg.T('Member Email',font='Calibri 11',key='-MFILTER-',enable_events=True, size=(20, 1)),
              ]]
    idx=0
    for member in members:
        if g.DEBUG_OL >= 2:
            print('MemberID',member[0],'\tProjectID',member[6],'\tTeam:',member[7])

        row = [sg.I(member[8],disabled=True, font='Calibri 11', size=(20,1)),
               sg.I(member[1],disabled=True, font='Calibri 11', size=(20,1)),
               sg.I(member[3],disabled=True, font='Calibri 11',size=(20,1)),
               sg.I(member[2],disabled=True, font='Calibri 11',size=(20,1)),
               sg.I(member[10],disabled=True, font='Calibri 11',size=(20,1)),
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

        if event1 == '-MFILTER-':
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


# In[ ]:


#list_roles_gui( 1, 3, "List of roles")


# In[ ]:


print(os.getcwd(),__name__,'imported')


# In[ ]:




