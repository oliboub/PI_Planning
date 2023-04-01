#!/usr/bin/env python
# coding: utf-8

# ## PI Roles Management

# In[ ]:


import global_variables as g
g.init()
import PySimpleGUI as sg
from backend_PI import * # Import tout ce qui est spécifique au projet
import os

if g.DEBUG_OL == -1:
    print("Debug mode active level :",g.DEBUG_OL)


# In[ ]:


connect('PIPlanning')


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

# In[1]:


def list_roles_gui(page,linespage=5,info='info'):
    if g.DEBUG_OL >= 1:
        print('--- function: list_roles_gui(',page,linespage,info,')')
 
    #    global page
    roles=[]
    rolesfiltered=[]
    rolestotal=[]
    
    rolestotal=Roles.objects(Archived=False).order_by('+RoleName')
#    rolestotal=roles1.sort(key = lambda elem: elem[1])
#    rolestotal.sort()

    items=len(rolestotal)

    start=page*linespage-linespage
    end=start+linespage
    if end > items:
        end = items
    a=0
 
    if g.DEBUG_OL >=2:
        print('items:',items,'\tstart:',start,'\tend:',end)
    

    for i in range(start,end):
        roles.append(rolestotal[i])
        if g.DEBUG_OL >= 2:
            print(roles[a])
        a=+1
    
    titlewindows='List of existing roles'
        
    sg.set_options(element_padding=(5, 5))
#    list_teams=list_teams_all()
    layout = [[sg.T(info,font=g.FONT,justification="left")],
              [sg.T('Role',font=g.FONT,key='-ROLE-',enable_events=False, size=(20, 1)),
               sg.T('Role Description',font=g.FONT,key='-DESC-',enable_events=False, size=(50, 2)),
               sg.T('Creation date',font=g.FONT,size=(20, 1)),
              ]]
    idx=0
    for role in roles:
        if g.DEBUG_OL >= 2:
            print('Role',role.RoleName) #,'\tRole',role[1],'\tDescription:',role[2],'\tCreation date:',role[4],)

        row = [sg.I(role.RoleName,disabled=True, font=g.FONT, size=(20,1)),
               sg.I(role.RoleDescription,disabled=True, font=g.FONT, size=(50,2)),
               sg.I(role.CreationDate,disabled=True, font=g.FONT,size=(20,1)),
            ]
        layout.append(row)
        idx+=1
   
    
    rolesqtt= [[sg.T('Total roles found: ',font=g.FONT, size=(15, 1)),sg.I(items,key='-RFOUND-',enable_events=False,disabled=True,visible=True,size=(10,1))]
                  ]
    
    displaylines= [[sg.T('Displayed Lines:',font=g.FONT, size=(17, 1)),sg.I(linespage,key='-DLINES-',enable_events=True,visible=True,size=(10,1))]
                  ]
    
    pagination = [[sg.B('<<', key='-BEGIN-',disabled=False),
                   sg.B("<", key='-BACK-',disabled=False),
                   sg.T(text=page, key='-PAGE-', size=(2, 1)),
                   sg.B(">", key='-NEXT-',disabled=False),
                   sg.B(">>", key='-END-',disabled=False)
                   ]]
    layout += [[sg.Col(displaylines, element_justification='left'),sg.Col(rolesqtt, element_justification='center'),sg.Col(pagination, justification='right')]]
    layout += [[sg.B('Return')]]
    
               
    window = MyWindow(titlewindows, layout,keep_on_top=True, element_justification = 'center',finalize=True)
    window.my_move_to_center()

    if g.DEBUG_OL >= 2:
        print('start',start,'end',end,'len(rolestotal)',len(rolestotal),'len(rolestotal)-linespage',len(rolestotal)-linespage)
    if end >= len(rolestotal):
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
                page=1
                window.close()
                list_roles_gui(page,linespage,info)
                                                  
        if event1 == "-NEXT-":
            page += 1
            window.close()
            list_roles_gui(page,linespage,info)

        if event1 == "-BACK-":
            page -= 1
            window.close()
            list_roles_gui(page,linespage,info)
        
        if event1 == "-BEGIN-":
            page = 1
            window.close()
            list_roles_gui(page,linespage,info)
        
        if event1 == "-END-":
            page = (items-linespage)//linespage+1
            window.close()
            list_roles_gui(page,linespage,info)


# In[ ]:


#list_roles_gui( 1, 3, "List of roles")


# In[ ]:


print(os.getcwd(),__name__,'imported')


# In[ ]:




