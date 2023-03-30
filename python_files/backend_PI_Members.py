#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Members

# ## prerequisites

# In[1]:


import global_variables as g
g.init()
import bcrypt
import os
from mongoengine import *
from backend_PI_mongo_model import *
from datetime import datetime

connect('PIPlanning')
if g.DEBUG_OL == -1:
    print("Debug mode active level :",g.DEBUG_OL)


# ## query_member(alias)

# In[6]:


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

# In[9]:


def query_member_alias(Alias):
    if g.DEBUG_OL >= 1:
        print('--- function: query_member_alias(',Alias,')')
    if type(Alias) is str:
        try:
            member1 = Members.objects(Archived=False,MemberAlias=Alias).first()
        except Exception as e:
            return "Error: %s" % (e)
            end()
    else:
        try:
            member1 = Members.objects(Archived=False,MemberID=Alias).first()
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
#    print(team.ProjectID)
    project=Projects.objects(ProjectID=team.ProjectID).first()
    debug_ol=0
    if g.DEBUG_OL >= 2:
        print('MemberID:',member1.MemberID)
        print('User Alias:',member1.MemberAlias)
        print('User Name:',member1.MemberName)
        print('User First Name:',member1.MemberFirstName)
        print('User Email:',member1.MemberEmail)
        print('Project allocated:',project.ProjectName)
        print('Project Team allocated:',team.TeamName)
        print('User Theme:',member1.MemberTheme)
        print('Team Role:',role.RoleName)
        print('Member admin:',member1.MemberAdmin)
        print('Member First Connection:',member1.MemberFirstConnection)
        
    
    return(member1.MemberID,member1.MemberName,member1.MemberAlias,member1.MemberFirstName,member1.MemberEmail,member1.MemberTheme,project.ProjectName,project.ProjectID,team.TeamName,role.RoleName,member1.MemberAdmin,member1.MemberFirstConnection)


# In[10]:


#query_member_alias(1)


# ## query_members_by_team(team)
# Team might be:
# - **All** for all
# - **TeamName**
# - **TeamID**
# 

# In[17]:


def query_members_by_team(team='All'):
    if g.DEBUG_OL >= 1:
        print('--- function: query_members_by_team(',team,')')

    membersid=[]
    members =[]
    members1=[]
    members2=[]
    member2=[]
    teamid=0
    
    if team == 'All':
        members1 = Members.objects(Archived=False)
        print(len(members1))

    if type(team) is str and team != 'All' :
        try:
            teamselected=Teams.objects(Archived=False,TeamName=team).first()
            teamid=teamselected.TeamID
            print(teamid)
        except Exception as e:
            return "Error: %s" % (e)
            end()
    elif type(team) is int:
        teamid=team
        
    if teamid != 0:
        members1=LinkMemberTeam.objects(TeamID=teamid)

    print('teamid:',teamid,'Qtt members found:',len(members1))      


    for i in members1:
        membersid.append(i.MemberID)
        print(membersid)
        
    for member in membersid:
        if g.DEBUG_OL >= 2:
                print(member)
        memberid,name,alias,firstname,email,theme,project,projectid,team,role,admin,firstcon=query_member_alias(member)
        member2=[memberid,name,alias,firstname,email,theme,project,projectid,team,role,admin,firstcon]
        if g.DEBUG_OL >= 2:
            print(member2)
        members.append(member2)
    
    return(members)


# In[20]:


#query_members_by_team(2)


# ## write_new_member_theme(memberid,theme)

# In[ ]:


def write_new_member_theme(memberid,theme):
    if g.DEBUG_OL >= 1:
        print('--- function: write_new_member_theme(',theme,')')
    member1 = Members.objects(MemberID=memberid).first()
    member1.MemberTheme=theme
    member1.save() 


# ## create_member(MemberName,FirstName.Email,MemberTheme)'lightblue2',ProjectName,TeamName,RoleName,admin=False)

# In[ ]:


def create_member(name,firstname,alias,email,theme,photo,projectid,teamid,roleid,password="default123",admin=False):
    if g.DEBUG_OL >= 1:
        print('--- function: create_member(',name,firstname,password,alias,email,theme,photo,projectid,teamid,roleid,admin,')')
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    member = Members()
    MemberName =  nameame
    MemberFirstName = firstname
    MemberEmail = email
    MemberAlias = alias
    MemberRole = roleid
    MemberTheme = theme
    MemberAvatar = photo
    hashAndSalt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    MemberPassword = hashAndSalt
    MemberAdmin = admin
    Archived = False
    CreationDate = creationdate
    LastUpdate = creationdate
    member.save()


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


print(os.getcwd(),__name__,'imported')


# In[ ]:




