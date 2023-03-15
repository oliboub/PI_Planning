#!/usr/bin/env python
# coding: utf-8

# ## PI User Management

# In[1]:


import PySimpleGUI as sg
from backend_PI import * # Import tout ce qui est spécifique au projet
from frontend_PI import *

global font
font='Calibri 11'
    
connect('PIPlanning')


# ------
# ### My Info
# #### Who am I

# In[2]:


def who_am_i_gui(alias):
    global admin
    print('function: who_am_i_gui(',alias,')')
    font='Calibri 11'
#    print(theme)
#    sg.theme(theme)
    memberid,name,firstname,email,theme,project,team,role,admin,firstcon=query_member_alias(alias)
    print(name,firstname,email,project,team,role,admin,firstcon)
    left_layout=[
        [sg.T('Alias Name', size=(10,1),font=font),sg.I(alias,key='-ALIAS-', size=(50,1),font=font)],
        [sg.T('First name', size=(10,1),font=font),sg.I(firstname,key='-FIRST-', size=(50,1),font=font)],
        [sg.T('Last name', size=(10,1),font=font),sg.I(name,key='-LAST-', size=(50,1),font=font)],
        [sg.T('Email', size=(10,1),font=font),sg.I(email,key='-EMAIL-', size=(50,1),font=font)]
    ]
    right_layout=[
        [sg.T('Project', size=(10,1),font=font),sg.I(project,key='-PROJ-', size=(50,1),font=font)],
        [sg.T('Team', size=(10,1),font=font),sg.I(team,key='-TEAM-', size=(50,1),font=font)],
        [sg.T('Team Role', size=(10,1),font=font),sg.I(role,key='-ROLE-', size=(50,1),font=font)],
    ]
    bottom_left=[[sg.T('UI Theme:', size=(10,1),font=font),sg.I(theme,key='-THEME-',size=(50,1),font=font)]]
    bottom_right=[[sg.T('Admin:', size=(10,1),font=font),sg.I('Yes',key='-ADMIN-',disabled=True,size=(10,1),font=font)]]
    bottom_sright=[[sg.B('Change password',key='-PASSWD-',size=(10,1),font=font)]]
    
    layout=[[[sg.Frame('User info',left_layout, vertical_alignment='center',pad=((15,15),(15,15))),
             sg.VerticalSeparator(),
             sg.Frame('Allocated Project Info',right_layout,element_justification='center',vertical_alignment='top',pad=((15,15),(15,15)))],
             sg.Frame('Application', bottom_left,element_justification='center',vertical_alignment='top',pad=((15,15),(15,15))),
             sg.B('Change password',key='-PASSWD-',size=(10,2)),
            sg.Frame('Admin',bottom_right,key='-FADMN-',element_justification='center',visible=False,vertical_alignment='top',pad=((15,15),(15,15)))],
             [sg.B('Return')]]
    
    window=MyWindow('Who am I',layout,finalize=True)
    window.my_move_to_center()
 
    if admin == True:
        window['-FADMN-'].update(visible=True)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == ('Return'):
            window.close()
            break
            
        if event == ('-PASSWD-'):
            print('Passwd')
            msg,firstcon = change_password(email,firstcon)
            print(msg)
            pass
            


# In[3]:


#who_am_i_gui('superadmin')


# ------
# ## Change Password

# In[14]:


def change_password(email,firstcon):
    print('function: change_password(',email,firstcon,')')
    font='Calibri 11'
    msg = 'Init'
    layout=[
        [sg.T('** First connection **',key='-FIRST-',size=(60,1),visible=False,justification='center',font=font)],
        [sg.T(email,size=(17,1),font=font),sg.T('please change your password',size=(25,1),font=font)],
        [sg.T('Old Passwd', key='-OLD1-',size=(15,1),visible=False,font=font),sg.I("",key='-OLDPWD-',  password_char='*',visible=False,size=(50,1),font=font)],
        [sg.T('New Passwd', size=(15,1),font=font),sg.I("",key='-NEWPWD-', password_char='*', size=(50,1),font=font)],
        [sg.T('Verify Passwd', size=(15,1),font=font),sg.I("",key='-CHKNEWPWD-', password_char='*', size=(50,1),font=font)],
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
            print('Cancel')
            window1.close()
            msg='Cancel:'
            return(msg,firstcon)
            
        elif event1 == 'Ok':
            if firstcon == False:
                print("firstcon = false")
                checkpwd=get_actual_password(email,values1['-OLDPWD-'])
                if checkpwd == False:
                    msg='error, actual password not matching'
                            
                else:    
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
            print("msg:",msg)
            matches = []
            errorlist= ['error, actual password not matching','error: old and new paswd are equivalents','error: new paswd are differents','error: new paswd is empty','error: Minimal size must be 8 caracters','Cancel:']
            matches = [match for match in errorlist if msg in match]
            print('matches:',matches)
            if matches :
                layout2=[[sg.T(msg,size=(60,1),justification='center',font=font)],[sg.B('Return')]]
                window2=MyWindow('Error',layout2,finalize=True)
                window2.my_move_to_center()
                
                while True:
                    event2, values2 = window2.read()
                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel' or event2 == 'Return':
                        print('Cancel')
                        window2.close()
                        break
 
            elif not matches:
                print('Passwd OK')
                aa=update_member_password(email,values1['-NEWPWD-'])
                print('Passwd updated')
                msg=('Ok: Password updated succesfully')
                firstcon=False
                window1.close()
                layout2=[[sg.T(msg,size=(60,1),justification='center',font=font)],[sg.B('Return')]]
                window2=MyWindow('Ok',layout2,finalize=True)
                window2.my_move_to_center()
                
                while True:
                    event2, values2 = window2.read()
                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel' or event2 == 'Return':
                        print('Cancel')
                        window2.close()
                        break
                break
    
    return(msg,firstcon)


# In[15]:


# change_password('oliboub@gmail.com',True)


# ### Select Theme

# In[6]:


def select_theme_gui(memberid,theme):
#    print('memberid:',memberid,' - theme',theme)
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

# In[3]:


def user_alias_gui():
    print('function: user_alias_gui()')
    layout=[
        [sg.T('Alias Name', size=(10,1)),sg.I(key='-ALIAS-', default_text='oliboub', size=(50,1))],
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
            print(result.MemberFirstConnection)
            print(result.MemberName)
            toto="Welcome back "+result.MemberFirstName
            sg.popup(toto,title="info",auto_close=True, auto_close_duration=2,)
            return(MemberAlias)


# ## Login_Window

# In[17]:


def login_window():
    print('function: login_window()')    
    x=3
    layout=[
        [sg.T('Email', font=font, size=(10,1)),sg.I(key='-EMAIL-', default_text='oliboub@gmail.com',font=font, size=(50,1))],
        [sg.T('Password', font=font,size=(10,1)),sg.I(key='-PASSWD-',font=font, password_char='*', size=(50,1))],
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
                    print(checkpasswd)
                    if checkpasswd == False:
                        layout=[
                            [sg.T("Wrong password. ",size=(20,1),font=font),sg.T(x,size=(3,1),font=font),sg.T('Remaining tries',size=(15,1),font=font)],
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
                        print(result.MemberFirstConnection)
                        MemberAlias= result.MemberAlias
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


# In[19]:


#global font
#font='Calibri 11'
# login_window()


# In[10]:


print(__name__,'imported')

