#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Members

# ## prerequisites

# In[1]:


import os
import bcrypt
from datetime import datetime
import PySimpleGUI as sg
from backend_PI_Utils import * # Import tout ce qui est spécifique au projet
from backend_PI_mongo_model import * # Import tout ce qui est spécifique au projet
#from backend_PI import * # Import tout ce qui est spécifique au projet
#from frontend_PI import *


# In[2]:


import global_variables as g
g.init()
connect('PIPlanning')


# ## query_member(alias)

# In[3]:


def query_member(alias):
    if g.DEBUG_OL >= 1:
        print('--- function: query_member(',alias,')')
    if g.DEBUG_OL >= 2:
#    if alias.find('@'):
        print(alias.find("@"))
    if alias.find('@') > -1:
        if g.DEBUG_OL >= 2:
            print('Email')
        member1 = Members.objects(Archived=False,MemberEmail=alias).first()
        if member1 is None:
            if g.DEBUG_OL >= 2:
                print('None')
            return(1,'None')
        else:
            if g.DEBUG_OL >= 2:
                print(member1.MemberName)
            return(0,member1)
        return(0,member1)        
    else:
        if g.DEBUG_OL >= 2:
            print('alias')
        member1 = Members.objects(Archived=False,MemberAlias=alias).first()
        if member1 is None:
            if g.DEBUG_OL >= 2:
                print('None')
            return(1,'None')
        else:
            if g.DEBUG_OL >= 2:
                print(member1.MemberName)
            return(0,member1)


# In[ ]:


#query_member('oliboub')


# ## query_member_alias(alias)
# Can be alias or ID

# In[4]:


def query_member_alias(Alias):
    if g.DEBUG_OL >= 1:
        print('--- function: query_member_alias(',Alias,')')
    
    if type(Alias) is str:
        try:
            member1 = Members.objects(MemberAlias=Alias).first()
        except Exception as e:
            return "Error: %s" % (e)
            end()
    else:
        try:
            member1 = Members.objects(MemberID=Alias).first()
        except Exception as e:
            return "Error: %s" % (e)
            end()
        
#    print('member1.MemberID',member1.MemberID)
#    print('member1.MemberName:',member1.MemberName)
#    linkrole=LinkMemberRole.objects(MemberID=member1.MemberID).first()
#    print(member1.MemberRole)
#    print(linkrole.RoleID)
    role=Roles.objects(RoleID=member1.MemberRole).first()
#    print(role.RoleName)
    link=LinkMemberTeam.objects(MemberID=member1.MemberID).first()
#    print(link.TeamID)
    team=Teams.objects(TeamID=link.TeamID).first()
#    print(team.TeamName)
#    print(team.TeamID)
#    print(team.ProjectID)
    project=Projects.objects(ProjectID=team.ProjectID).first()
    debug_ol=0
    if g.DEBUG_OL >= 2:
        print('MemberID:',member1.MemberID)
        print('Member Name:',member1.MemberName)
        print('Member Alias:',member1.MemberAlias)
        print('Member First Name:',member1.MemberFirstName)
        print('Member Email:',member1.MemberEmail)
        print('Member Theme:',member1.MemberTheme)
        print('Member admin:',member1.MemberAdmin)
        print('Member Portfolio:',member1.MemberPortfolio)
        print('Member status:',member1.Archived)
        print('Member lastupdate:',member1.LastUpdate)
        print('Member First Connection:',member1.MemberFirstConnection)
        print('Project ID:',project.ProjectID)
        print('Project allocated:',project.ProjectName)
        print('Team ID:',team.TeamID)
        print('Role ID:',role.RoleID)
        print('Team allocated:',team.TeamName)
        print('Role:',role.RoleName)
        
    
    return(member1.MemberID,member1.MemberName,member1.MemberAlias,member1.MemberFirstName,member1.MemberEmail,member1.MemberTheme,member1.MemberAdmin,member1.MemberPortfolio,member1.Archived,member1.LastUpdate,member1.MemberFirstConnection,project.ProjectID,project.ProjectName,team.TeamID,team.TeamName,role.RoleID,role.RoleName)


# In[ ]:


#query_member_alias(11)


# ## list_members_by_team(team)
# Team might be:
# - **All** for all
# - **TeamName**
# - **TeamID**
# 

# In[5]:


def list_members_by_team(team=None):
    if g.DEBUG_OL >= 1:
        print('--- function: list_members_by_team(',team,')')

    membersid=[]
    members =[]
    members1=[]
    members2=[]
    member2=[]
    teamid=0
    
    if team == None:
        members1 = Members.objects()
        if g.DEBUG_OL >= 2:
            print(len(members1))

    elif type(team) is str and team != None :
        try:
            teamselected=Teams.objects(TeamName=team).first()
            teamid=teamselected.TeamID
            if g.DEBUG_OL >= 2:
                print(teamid)
        except Exception as e:
            return "Error: %s" % (e)
            end()
    elif type(team) is int:
        teamid=team
    
    if g.DEBUG_OL >= 2:
        print('Teamid:',teamid)
    
    if teamid != 0:
        members1=LinkMemberTeam.objects(TeamID=teamid)
        if len(members1) == 0:
            return "Error: Team has no members"

        if g.DEBUG_OL >= 2:
            print('teamid:',teamid,'Qtt members found:',len(members1))      


    for i in members1:
        membersid.append(i.MemberID)
        if g.DEBUG_OL >= 2:
            print(membersid)
        
    for member in membersid:
        if g.DEBUG_OL >= 2:
                print(member)
        memberid,name,alias,firstname,email,theme,admin,portfolio,status,lastupdate,firstcon,projectid,project,teamid,team,roleid,role=query_member_alias(member)
        member2=[memberid,name,alias,firstname,email,theme,admin,portfolio,status,lastupdate,firstcon,projectid,project,teamid,team,roleid,role]
        if g.DEBUG_OL >= 2:
            print(member2)
        members.append(member2)
    
    return(members)


# In[7]:


#list_members_by_team()
#list_members_by_team('applepie')


# ## create_member(MemberName,FirstName.alias,email,teamid,roleid,MemberTheme='lightblue2',password='default123',admin=False)

# In[ ]:


def create_member(name,firstname,alias,email,teamid,roleid,theme='LightBlue2',password="default123",admin=False):
    if g.DEBUG_OL >= 1:
        print('--- function: create_member(',name,firstname,alias,email,teamid,roleid,theme,password,admin,')')
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    member = Members()
    member.MemberName =  name
    member.MemberFirstName = firstname
    member.MemberEmail = email
    member.MemberAlias = alias
    member.MemberRole = roleid
    member.MemberTheme = theme
#    MemberAvatar = photo
    hashAndSalt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    member.MemberPassword = hashAndSalt
    member.MemberAdmin = admin
    member.Archived = False
    member.MemberFirstConnection=True
    member.CreationDate = creationdate
    member.LastUpdate = creationdate
    member.save()
    
    newmember=Members.objects(MemberAlias=alias).first()
    if g.DEBUG_OL >= 2:
        print('New member created with memberID=',newmember.MemberID)
    
    teammember= LinkMemberTeam()
    teammember.MemberID = newmember.MemberID
    teammember.TeamID = teamid
    teammember.save()
    
    if g.DEBUG_OL >= 2:
        print('newmember:',alias,' is allocated to teamid:',teamid)
    return newmember.MemberID


# In[ ]:


#create_member('Artic', 'Haud','haudartic','haudartic@toto.com',2,2)


# ## archive_member(memberid,newstatus)

# In[ ]:


def archive_member(memberid,newstatus):
    if g.DEBUG_OL >= 1:
        print('--- function: archive_member(',memberid,newstatus,')')
    item=Members.objects(MemberID=memberid).first()
    if g.DEBUG_OL >= 2:
        print('archive member name:',item.MemberName)
    now = datetime.now()
    item.Archived = newstatus
    item.LastUpdate = now.strftime("%d/%m/%Y %H:%M:%S")
    item.save()


# In[ ]:


#archive_member(2,False)


# ## update_member(memberid,teamid,name,firstname,alias,email,roleid)

# In[ ]:


def update_member(memberid,teamid,name,firstname,alias,email,roleid):
    if g.DEBUG_OL >= 1:
        print('--- function: update_member(',memberid,teamid,name,firstname,alias,email,roleid,')')
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    item=Members.objects(MemberID=memberid).first()
    item.MemberName =  name
    item.MemberFirstName = firstname
    item.MemberEmail = email
    item.MemberAlias = alias
    item.MemberRole = roleid
#    MemberAvatar = photo
    item.LastUpdate = creationdate
    item.save()
    
    teammember= LinkMemberTeam.objects(MemberID=memberid).first()
    teammember.TeamID = teamid
    teammember.save()
    
    if g.DEBUG_OL >= 2:
        print('newmember:',alias,' is updated')
    return memberid


# ------

# ## write_new_member_theme(memberid,theme)

# In[ ]:


def write_new_member_theme(memberid,theme):
    if g.DEBUG_OL >= 1:
        print('--- function: write_new_member_theme(',memberid,theme,')')
    member1 = Members.objects(MemberID=memberid).first()
    member1.MemberTheme=theme
    member1.save() 


# ## update_member_password(email,password)

# In[ ]:


def update_member_password(email,password):
    if g.DEBUG_OL >= 1:
        print('--- function: update_member_passwd(',email,'password',')',)
    member1 = Members.objects(Archived=False,MemberEmail=email).first()
    debug_ol=0
    if g.DEBUG_OL >= 2:
        print('------ Before')
        print('MemberID:',member1.MemberID)
        print('User Alias:',member1.MemberAlias)
        print('User Name:',member1.MemberName)
        print('User First Name:',member1.MemberFirstName)
        print('User Email:',member1.MemberEmail)
        print('Member First Connection:',member1.MemberFirstConnection)
        print('Member Last Update:',member1.LastUpdate)
        print('Member Password:',member1.MemberPassword)
   
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    hashAndSalt = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
##    Static mode
##    member1.update(MemberPassword = hashAndSalt,member1.update(MemberFirstConnection = False,member1.update(LastUpdate = creationdate)
    

## Dynamic mode
    fields = {
        'MemberPassword': hashAndSalt,
        'MemberFirstConnection': False,
        'LastUpdate': creationdate
    }
    member1.update(**fields)

    member1 = Members.objects(Archived=False,MemberEmail=email).first()
    if g.DEBUG_OL >= 2:
        print('------ After')
        print('MemberID:',member1.MemberID)
        print('User Alias:',member1.MemberAlias)
        print('User Name:',member1.MemberName)
        print('User First Name:',member1.MemberFirstName)
        print('User Email:',member1.MemberEmail)
        print('Member First Connection:',member1.MemberFirstConnection)
        print('Member Last Update:',member1.LastUpdate)
        print('Member Password:',member1.MemberPassword)


# In[ ]:


#update_member_password('oliboub@gmail.com','aaaaaaaa')


# ## get_actual_password(email,passwd)

# In[ ]:


def get_actual_password(email,passwd):
    if g.DEBUG_OL >= 1:
        print('--- function: get_actual_password(',email,'password)',)
    password=passwd.encode('utf-8')
    strikepwd= bcrypt.hashpw(password, bcrypt.gensalt())
    
    member1 = Members.objects(Archived=False,MemberEmail=email).first()

    if g.DEBUG_OL >= 2:
        print('strikepwd:',strikepwd)
        print('MemberID:',member1.MemberID)
        print('User Alias:',member1.MemberAlias)
        print('User Name:',member1.MemberName)
        print('User First Name:',member1.MemberFirstName)
        print('User Email:',member1.MemberEmail)
        print('Member First Connection:',member1.MemberFirstConnection)
        print('Member Last Update:',member1.LastUpdate)
        print('Member Password:',member1.MemberPassword)
    
    if bcrypt.hashpw(password, member1.MemberPassword) == member1.MemberPassword:
        if g.DEBUG_OL >= 2:
            print("It matches")
        a=True
    else:
        if g.DEBUG_OL >= 2:
            print("It does not match")
        a=False
    return(a)


# In[ ]:


#get_actual_password('admin@gmail.com','aaaaaaaa')


# In[ ]:


#list_members_page(1,5,1)


# In[ ]:


if g.DEBUG_OL >= 1:
    print(os.getcwd(),__name__,'imported')

