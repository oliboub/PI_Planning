#!/usr/bin/env python
# coding: utf-8

# ## PI User Management

# In[7]:


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


# In[8]:


from frontend_PI_Utils import *


# In[9]:


connect('PIPlanning')


# ------
# ### My Info
# #### Who am I

# In[13]:


def who_am_i_gui(alias):

    global admin
    if g.DEBUG_OL >= 1:
        print('function: who_am_i_gui(',alias,')')
#    font='Calibri 11'
#    print(theme)
#    sg.theme(theme)
    memberid,name,alias,firstname,email,theme,admin,portfolio,status,lastupdate,firstcon,projectid,project,teamid,team,roleid,role=query_member_alias(alias)
    if g.DEBUG_OL >= 2:
        print(memberid,name,alias,firstname,email,theme,admin,portfolio,status,lastupdate,firstcon,projectid,project,teamid,team,roleid,role)
    left_layout=[
        [sg.T('Alias Name', size=(10,1),font=g.FONT),sg.I(alias,key='-ALIAS-',enable_events=False,disabled=True, size=(50,1),font=g.FONT)],
        [sg.T('First name', size=(10,1),font=g.FONT),sg.I(firstname,key='-FIRST-', enable_events=False,disabled=True,size=(50,1),font=g.FONT)],
        [sg.T('Last name', size=(10,1),font=g.FONT),sg.I(name,key='-LAST-', enable_events=False,disabled=True,size=(50,1),font=g.FONT)],
        [sg.T('Email', size=(10,1),font=g.FONT),sg.I(email,key='-EMAIL-', enable_events=False,disabled=True,size=(50,1),font=g.FONT)]
    ]
    right_layout=[
        [sg.T('Project', size=(10,1),font=g.FONT),sg.I(project,key='-PROJ-',enable_events=False,disabled=True, size=(50,1),font=g.FONT)],
        [sg.T('Team', size=(10,1),font=g.FONT),sg.I(team,key='-TEAM-',enable_events=False, disabled=True,size=(50,1),font=g.FONT)],
        [sg.T('Team Role', size=(10,1),font=g.FONT),sg.I(role,key='-ROLE-', enable_events=False,disabled=True,size=(50,1),font=g.FONT)],
    ]
    bottom_left=[[sg.T('UI Theme:', size=(10,1),font=g.FONT),sg.I(theme,key='-THEME-',enable_events=False,disabled=True,size=(50,1),font=g.FONT)]]
    bottom_right=[[sg.T('Admin:', size=(10,1),font=g.FONT),sg.I('Yes',key='-ADMIN-',enable_events=False,disabled=True,size=(10,1),font=g.FONT)]]
    bottom_2right=[[sg.T('Portfolio:', size=(10,1),font=g.FONT),sg.I('Yes',key='-PORTFOLIO-',enable_events=False,disabled=True,size=(10,1),font=g.FONT)]]
    bottom_sright=[[sg.B('Change password',key='-PASSWD-',size=(10,1),font=g.FONT)]]
    
    layout=[[[sg.Frame('User info',left_layout, vertical_alignment='center',pad=((15,15),(15,15))),
             sg.VerticalSeparator(),
             sg.Frame('Allocated Project Info',right_layout,element_justification='center',vertical_alignment='top',pad=((15,15),(15,15)))],
             sg.Frame('Application', bottom_left,element_justification='center',vertical_alignment='top',pad=((15,15),(15,15))),
             sg.B('Change password',key='-PASSWD-',size=(10,2)),
             sg.Frame('Admin',bottom_right,key='-FADMN-',element_justification='center',visible=False,vertical_alignment='top',pad=((15,15),(15,15))),
             sg.Frame('Portfolio',bottom_2right,key='-FPORTF-',element_justification='center',visible=False,vertical_alignment='top',pad=((15,15),(15,15)))],
             [sg.B('Return')]]
    
    window=MyWindow('Who am I',layout,finalize=True)
    window.my_move_to_center()
 
    if admin == True:
        window['-FADMN-'].update(visible=True)
        
    if portfolio == True:
        window['-FPORTF-'].update(visible=True)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == ('Return'):
            window.close()
            break
            
        if event == ('-PASSWD-'):
            if g.DEBUG_OL >= 2:
                print('Passwd')
            msg,firstcon = change_password(email,firstcon)
            if g.DEBUG_OL >= 2:
                print(msg)
            pass            


# In[18]:


#who_am_i_gui('scrumol')
#who_am_i_gui('admintop')
#who_am_i_gui('rtelead')


# ------
# ### Change Password

# In[ ]:


def change_password(email,firstcon):
    if g.DEBUG_OL >= 1:
        print('function: change_password(',email,firstcon,')')
    font='Calibri 11'
    msg = 'Init'
    layout=[
        [sg.T('** First connection **',key='-FIRST-',size=(60,1),visible=False,justification='center',font=g.FONT)],
        [sg.T(email,size=(17,1),font=g.FONT),sg.T('please change your password',size=(25,1),font=g.FONT)],
        [sg.T('Old Passwd', key='-OLD1-',size=(15,1),visible=False,font=g.FONT),sg.I("",key='-OLDPWD-',  password_char='*',visible=False,size=(50,1),font=g.FONT)],
        [sg.T('New Passwd', size=(15,1),font=g.FONT),sg.I("",key='-NEWPWD-', password_char='*', size=(50,1),font=g.FONT)],
        [sg.T('Verify Passwd', size=(15,1),font=g.FONT),sg.I("",key='-CHKNEWPWD-', password_char='*', size=(50,1),font=g.FONT)],
        [sg.Ok(),sg.Cancel()]]
 
    window1=MyWindow('Change Password',layout,finalize=True)
    window1.my_move_to_center()
 
    if firstcon == False:
        window1['-OLD1-'].update(visible=True)
        window1['-OLDPWD-'].update(visible=True)
    if firstcon == True:
        window1['-FIRST-'].update(visible=True)

    while True:
        event1, values1 = window1.read()
        if event1 == sg.WIN_CLOSED or event1 == 'Cancel':
            if g.DEBUG_OL >= 2:
                print('Cancel')
            window1.close()
            msg='Cancel:'
            return(msg,firstcon)
            
        elif event1 == 'Ok':
            if firstcon == False:
                if g.DEBUG_OL >= 2:
                    print("firstcon = false")
                checkpwd=get_actual_password(email,values1['-OLDPWD-'])
                if checkpwd == False:
                    msg='error, actual password not matching'
                            
                else:    
                    if g.DEBUG_OL >= 2:
                        print('check old passwd OK')
                    if values1['-NEWPWD-'] == values1['-OLDPWD-'] and firstcon == True:
                        msg='error: old and new paswd are equivalents'
#                window1.close()
 
                    elif values1['-CHKNEWPWD-'] != values1['-NEWPWD-']:
                        msg='error: new paswd are differents'
#                window1.close()
           
                    elif values1['-CHKNEWPWD-'] == '':
                        msg='error: new paswd is empty'
#                window1.close()
 
                    elif len(values1['-NEWPWD-']) < 8:
#                        print(len(values1['-NEWPWD-']))
                        msg='error: Minimal size must be 8 caracters'
#                window1.close()

                    else:
                        msg='ok: Passwd migth be updated'
#                    print(values1['-CHKNEWPWD-'],values1['-NEWPWD-'])
#                window1.close()
#            pass
            if g.DEBUG_OL >= 2:
                print("msg:",msg)
            matches = []
            errorlist= ['error, actual password not matching','error: old and new paswd are equivalents','error: new paswd are differents','error: new paswd is empty','error: Minimal size must be 8 caracters','Cancel:']
            matches = [match for match in errorlist if msg in match]
            if g.DEBUG_OL >= 2:
                print('matches:',matches)
            if matches :
                layout2=[[sg.T(msg,size=(60,1),justification='center',font=g.FONT)],[sg.B('Return')]]
                window2=MyWindow('Error',layout2,finalize=True)
                window2.my_move_to_center()
                
                while True:
                    event2, values2 = window2.read()
                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel' or event2 == 'Return':
                        if g.DEBUG_OL >= 2:
                            print('Cancel')
                        window2.close()
                        break
 
            elif not matches:
                if g.DEBUG_OL >= 2:
                    print('Passwd OK')
                aa=update_member_password(email,values1['-NEWPWD-'])
                if g.DEBUG_OL >= 2:
                    print('Passwd updated')
                msg=('Ok: Password updated succesfully')
                firstcon=False
                window1.close()
                layout2=[[sg.T(msg,size=(60,1),justification='center',font=g.FONT)],[sg.B('Return')]]
                window2=MyWindow('Ok',layout2,finalize=True)
                window2.my_move_to_center()
                
                while True:
                    event2, values2 = window2.read()
                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel' or event2 == 'Return':
                        if g.DEBUG_OL >= 2:
                            print('Cancel')
                        window2.close()
                        break
                break
    
    return(msg,firstcon)


# In[ ]:


# change_password('oliboub@gmail.com',True)


# ### Select Theme

# In[ ]:


def select_theme_gui(memberid,theme):
    if g.DEBUG_OL >= 1:
        print('function: select_theme_gui(',memberid,theme,')')

    if g.DEBUG_OL >= 2:
        print('memberid:',memberid,' - theme',theme)
    sg.theme(theme)

    layout = [[sg.T('This is your layout')],
              [sg.Button('Ok'), sg.Button('Change Theme'), sg.Button('Exit')]]
    window=MyWindow('Pattern for changing theme', layout,finalize=True)
    window.my_move_to_center()
    
    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            window.close()
            return(theme)
        
        if event == 'Change Theme':      # Theme button clicked, so get new theme and restart window
            window1 = MyWindow('Choose Theme',
            [[sg.Combo(sg.theme_list(), readonly=True, k='-THEME LIST-'),
             sg.OK(), sg.Cancel()]],
             finalize=True)
            window1.my_move_to_center()
                
            event, value = window1.read(close=True)
            
            if event == 'OK':
 # ---- Switch to your new theme! ---- IMPORTANT PART OF THE PROGRA<
                window.close()
                theme=value['-THEME LIST-']
                write_new_member_theme(memberid,theme)
                sg.theme(theme)
                return(theme)    


# ### Call User Alias

# In[1]:


def user_alias_gui():
    if g.DEBUG_OL >= 1:
        print('function: user_alias_gui()')
    layout=[
        [sg.T('Alias Name', size=(10,1)),sg.I(key='-ALIAS-', default_text='', size=(50,1))],
        [sg.OK(),sg.Cancel()]
    ]
    
    window=MyWindow('Enter your alias',layout,finalize=True)
    window.my_move_to_center()
    
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == ('Cancel'):
            window.close()
            MemberAlias='None'
            return(MemberAlias) 
            break
        
        elif event =='OK':
            if g.DEBUG_OL >= 2:
                print(value['-ALIAS-'])
            window.close()
            MemberAlias= value['-ALIAS-']
            break
    
    if MemberAlias != 'None':
        valid,result=query_member(MemberAlias)
        if valid == 1:
            layout=[
                [sg.T("Alias is not existing in database.\nThanks to check with your administrator")],
                [sg.Cancel()]]
            window1=MyWindow('Error',layout,finalize=True)
            window1.my_move_to_center()
            
            while True:
                event1, value1 = window1.read()
                if event1 == sg.WIN_CLOSED or event1 == ('Cancel'):
                    window1.close()
                    MemberAlias='None'
                    return(MemberAlias)                    
                    break

      
        else:
            if g.DEBUG_OL >= 2:
                print(result.MemberFirstConnection)
                print(result.MemberName)
            toto="Welcome back "+result.MemberFirstName
            sg.popup(toto,title="info",auto_close=True, auto_close_duration=2,)
            return(MemberAlias)


# ## Login_Window

# In[ ]:


def login_window():
    if g.DEBUG_OL >= 1:
        print(g.FONT,g.DEBUG_OL)
        print('function: login_window()')    
    x=3
    layout=[
        [sg.T('Email', font=g.FONT, size=(10,1)),sg.I(key='-EMAIL-', default_text='admin@toto.com',font=g.FONT, size=(50,1))],
        [sg.T('Password', font=g.FONT,size=(10,1)),sg.I(key='-PASSWD-',font=g.FONT, password_char='*', size=(50,1))],
        [sg.OK(),sg.Cancel()]
    ]
    
    window=MyWindow('Login Session',layout,finalize=True)
    window.my_move_to_center()
    
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == ('Cancel'):
            window.close()
            MemberEmail='None'
            return(MemberEmail)
            break
        
        elif event =='OK':
            if g.DEBUG_OL >= 2:
                print(value['-EMAIL-'])
#            window.close()
            MemberEmail= value['-EMAIL-']

            if MemberEmail != 'None':
                valid,result=query_member(MemberEmail)
                if valid == 1:
                    layout=[
                        [sg.T("Email is not existing in database.\nThanks to check with your administrator")],
                        [sg.Cancel()]]

                    window1=MyWindow('Error',layout,finalize=True)
                    window1.my_move_to_center()

                    while True:
                        event1, value1 = window1.read()
                        if event1 == sg.WIN_CLOSED or event1 == ('Cancel'):
                            window1.close()
                            break
       
                else:
                    checkpasswd=get_actual_password(value['-EMAIL-'],value['-PASSWD-'])
                    if g.DEBUG_OL >= 2:
                        print(checkpasswd)
                    if checkpasswd == False:
                        layout=[
                            [sg.T("Wrong password. ",size=(20,1),font=g.FONT),sg.T(x,size=(3,1),font=g.FONT),sg.T('Remaining tries',size=(15,1),font=g.FONT)],
                            [sg.Cancel()]]

                        window1=MyWindow('Error',layout,finalize=True)
                        window1.my_move_to_center()

                        while True:
                            event1, value1 = window1.read()
                            if event1 == sg.WIN_CLOSED or event1 == ('Cancel'):
                                window1.close()
                                break

                        if x == 0:
                            window.close()
                            return('None')
                        x -= 1

                    else:
                        if g.DEBUG_OL >= 2:
                            print(result.MemberFirstConnection)
                        MemberAlias= result.MemberAlias
                        if g.DEBUG_OL >= 2:
                            print(MemberAlias)
                        window.close()
                        if result.MemberFirstConnection == True:
                            result = change_password(MemberEmail,True)
                            toto="Welcome  "+MemberAlias
                            sg.popup(toto,title="info",auto_close=True, auto_close_duration=2,)
                        else:
                            toto="Welcome back "+MemberAlias
                            sg.popup(toto,title="info",auto_close=True, auto_close_duration=2,)
                        return(MemberAlias)


# In[ ]:


#global font
#font='Calibri 11'
# login_window()


# In[ ]:


if g.DEBUG_OL >= 1:
    print(os.getcwd(),__name__,'imported')

