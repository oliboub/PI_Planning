#!/usr/bin/env python
# coding: utf-8

# ## PI Project Management

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
from backend_PI_Projects import * # Import tout ce qui est spécifique au projet
from backend_PI_Tasks import * # Import tout ce qui est spécifique au projet
from backend_PI_Teams import * # Import tout ce qui est spécifique au projet


# In[2]:


from frontend_PI_Utils import *


# In[3]:


connect('PIPlanning')


# ### Create project

# In[ ]:


def create_project_gui(info='info'):
    if g.DEBUG_OL >= 1:
        print('--- function: create_project_gui(',info,')')
    
    sg.set_options(element_padding=(5, 10))

    existingprojects=[]
    
    projects=Projects.objects()
    for i in projects:
        existingprojects.append(i.ProjectName.lower())
    if g.DEBUG_OL >= 2:
        print(existingprojects)
     
    layout = [
        [sg.T(info,font=g.FONT,justification="left")],
        [sg.T('project Name',font=g.FONT,size=(20, 1)), sg.I("new project",key='-PROJECT-',visible=True,font=g.FONT+' italic', size=(20,1))],
        [sg.T('Project Description',font=g.FONT, size=(20, 1)), sg.I("Description",visible=True,key='-DESC-',font=g.FONT+' italic',size=(20,1))],
        [sg.B('Add', enable_events=True), sg.Cancel()]
    ]
    window = MyWindow('Create Project', layout,finalize=True)
    window.my_move_to_center()

    while True:
        event, values = window.read()
        if g.DEBUG_OL >= 2:
            print(event,values)
            
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            break
            
        if event == 'Add':
            if values['-PROJECT-'].lower() in existingprojects:
                sg.popup('Project '+values['-PROJECT-']+'  already exists !',title="info",auto_close=True, auto_close_duration=3,)
                window['-PROJECT-'].update("new project")
 

            elif values['-DESC-'] == "Description":
                sg.popup('Please enter a description',title="info",auto_close=True, auto_close_duration=3,)
 
            else:
                id=create_project(values['-PROJECT-'], values['-DESC-'])
                if g.DEBUG_OL >= 2:
                    print('New project: '+values['-PROJECT-']+' created with id:',str(id))
                sg.popup('New project: '+values['-PROJECT-']+' created with id: '+str(id),title="info",auto_close=True, auto_close_duration=3,)
                window.close()
                break


# In[ ]:


#create_project_gui("Creation d'un nouveau projet")


# ### list_projects_gui(page=1,linespage=5,info)

# In[4]:


def list_projects_gui(page=1,linespage=5,info='info'):
    if g.DEBUG_OL >= 1:
        print('--- function: list_projects_gui(',page,linespage,info,')')
 
    #    global page
    projects=[]
    projectsfiltered=[]
    projectstotal=[]
    
    projectstotal=Projects.objects().order_by('+ProjectName')
#    projectstotal=projects1.sort(key = lambda elem: elem[1])
#    projectstotal.sort()

    items=len(projectstotal)

    start=page*linespage-linespage
    end=start+linespage
    if end > items:
        end = items
    a=0
 
    if g.DEBUG_OL >=2:
        print('items:',items,'\tstart:',start,'\tend:',end)
    

    for i in range(start,end):
        projects.append(projectstotal[i])
        if g.DEBUG_OL >= 2:
            print(projects[0]) #.ProjectID,projects.ProjectName)
        a=+1
    
    titlewindows='List of existing projects'
        
    sg.set_options(element_padding=(5, 5))
#    list_teams=list_teams_all()
    layout = [[sg.T(info,font=g.FONT,justification="left")],
              [sg.T('Project',font=g.FONT,enable_events=False, size=(20, 1)),
               sg.T('Project Description',font=g.FONT,key='-DESC-',enable_events=False, size=(50, 2)),
               sg.T('Last Update',font=g.FONT,size=(20, 1)),
               sg.T('Update',font=g.FONT,size=(10, 1)),
               sg.T(' ',font=g.FONT,size=(5, 1)),
               sg.T('Status',font=g.FONT,size=(10, 1))
              ]]
    idx=0
    for project in projects:
        if g.DEBUG_OL >= 2:
            print('Project',project.ProjectName ,'\tProjectID',project.ProjectID ,'\tProject Status',project.Archived) #,'\tDescription:',project[2],'\tCreation date:',project[4],)
        if project.Archived is False:
            status='Active'
            FONT1=g.FONT
            bfcolor='white'
            bbcolor='green'
        else:
            status='Archived'
            FONT1=g.FONT+' italic'
            bfcolor='white'
            bbcolor='firebrick3'
    
        row = [sg.T(project.ProjectID,visible=False),
                sg.I(project.ProjectName,key=f'-PNAME-{project.ProjectID}',disabled=False, font=g.FONT, size=(20,1)),
               sg.I(project.ProjectDescription,key=f'-DESC-{project.ProjectID}',disabled=False, font=g.FONT, size=(50,2)),
               sg.I(project.LastUpdate,disabled=False, font=g.FONT,size=(20,1)),
               sg.B('Update',enable_events=True, key=f'-UPDT-{project.ProjectID}',font=g.FONT,button_color=('white','darkblue'),size=(10,1)),
               sg.T(' ',font=g.FONT,size=(5, 1)),
               sg.B(status, enable_events=True,key=f'-ARCH-{project.ProjectID}',font=FONT1,button_color=(bfcolor,bbcolor),size=(10,1)),
            ]
        layout.append(row)
        idx+=1
   
    
    projectsqtt= [[sg.T('Total projects found: ',font=g.FONT, size=(15, 1)),sg.I(items,key='-PFOUND-',enable_events=False,disabled=True,visible=True,size=(10,1))]
                  ]
    
    displaylines= [[sg.T('Displayed Lines:',font=g.FONT, size=(17, 1)),
                    sg.I(linespage,key='-DLINES-',enable_events=True,visible=True,size=(10,1)),
                   sg.T(' ',font=g.FONT,size=(10, 1))]
                   ]
    
    pagination = [[sg.B('<<', key='-BEGIN-',disabled=False),
                   sg.B("<", key='-BACK-',disabled=False),
                   sg.T(text=page, key='-PAGE-', size=(2, 1)),
                   sg.B(">", key='-NEXT-',disabled=False),
                   sg.B(">>", key='-END-',disabled=False)
                   ]]
    
    createproject = [[sg.B('Create Project',key='-CPROJECT-',font=g.FONT,button_color=('white','darkblue')),
                   sg.T(' ',font=g.FONT,size=(12, 1))]]
    
    
    layout += [[sg.Col(createproject, element_justification='left'),sg.Col(displaylines,element_justification='center'), sg.Col(projectsqtt, element_justification='center'),sg.Col(pagination, justification='right')]]
    layout += [[sg.B('Return',font=g.FONT)]]
    
               
    window = MyWindow(titlewindows, layout,keep_on_top=True, element_justification = 'center',finalize=True)
    window.my_move_to_center()

    if g.DEBUG_OL >= 2:
        print('start',start,'end',end,'len(projectstotal)',len(projectstotal),'len(projectstotal)-linespage',len(projectstotal)-linespage)
    if end >= len(projectstotal):
        window['-END-'].update(disabled=True)
        window['-NEXT-'].update(disabled=True)
    if start  < linespage:
        window['-BEGIN-'].update(disabled=True)
        window['-BACK-'].update(disabled=True)

    
    while True:
        event1, values1 = window.read()
        if g.DEBUG_OL >=2:
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
                list_projects_gui(page,linespage,info)
                                                  
        if event1 == "-NEXT-":
            page += 1
            window.close()
            list_projects_gui(page,linespage,info)

        if event1 == "-BACK-":
            page -= 1
            window.close()
            list_projects_gui(page,linespage,info)
        
        if event1 == "-BEGIN-":
            page = 1
            window.close()
            list_projects_gui(page,linespage,info)
        
        if event1 == "-END-":
            page = (items-linespage)//linespage+1
            window.close()
            list_projects_gui(page,linespage,info)
            
        if event1 == "-CPROJECT-":
            window.close()
            create_project_gui()
            page = 1
            list_projects_gui(page,linespage,info)
            
        if '-ARCH-' in event1:
            a=int(event1.split("-")[-1])
            itemstatus=Projects.objects(ProjectID=a).first()
            print(itemstatus.Archived)
            if itemstatus.Archived == False:
                newstatus=True
            else:
                newstatus=False
                
            if g.DEBUG_OL >= 2:
                print(a,newstatus)
            archive_project(a,newstatus)
            page = 1
            window.close()
            list_projects_gui(page,linespage,info)

        if '-UPDT-' in event1:
            a=int(event1.split("-")[-1])
            itemupd=Projects.objects(ProjectID=a).first()
            if g.DEBUG_OL >= 2:
                print(itemupd.ProjectName,itemupd.ProjectID)
            proj='-PNAME-'+str(itemupd.ProjectID)
            desc='-DESC-'+str(itemupd.ProjectID)

            if g.DEBUG_OL >= 2:
                print(itemupd.ProjectID,"- '",values1[proj],"' - '",values1[desc],"'")
            update_project(a,values1[proj],values1[desc])
            page = 1
            window.close()
            list_projects_gui(page,linespage,info)


# In[5]:


#list_projects_gui()


# In[ ]:


if g.DEBUG_OL >= 1:
    print(os.getcwd(),__name__,'imported')

