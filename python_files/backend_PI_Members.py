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


# ## query_member(alias)

# In[2]:


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


# ## query_members_alias(alias)
# Can be alias or ID

# In[3]:


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
        
    
    return(member1.MemberID,member1.MemberName,member1.MemberFirstName,member1.MemberEmail,member1.MemberTheme,project.ProjectName,project.ProjectID,team.TeamName,role.RoleName,member1.MemberAdmin,member1.MemberFirstConnection)


# In[ ]:


#query_member_alias(5)


# ## query_members_by_team(team)
# Team might be:
# - **All** for all
# - **TeamName**
# - **TeamID**
# 

# In[ ]:


def query_members_by_team(team='All'):
    if g.DEBUG_OL >= 1:
        print('--- function: query_members_by_team(',team,')')
    members = []
    if team is None:
        if g.DEBUG_OL >= 2:
            print('Please add a teamname as parameter')
        return('[]')

    else:
        if team != 'All':
            if type(team) is int:
                teams=Teams.objects(TeamID=team).first()
            else:
                teams=Teams.objects(TeamName=team).first()
            if g.DEBUG_OL >= 2:
                print(teams)

            if teams is None:
                if g.DEBUG_OL >= 2:
                    print("'None' value provided for item of farkling routine")
                return('[]')

            else:
                link=LinkMemberTeam.objects(TeamID=teams.TeamID)
                if g.DEBUG_OL >= 2:
                    print('link:',link)
        else:
            link=LinkMemberTeam.objects()
            
        for i in range(len(link)):
            member1=Members.objects(MemberID=link[i].MemberID).first()
            #if g.DEBUG_OL >= 2:
            #    print(, link[i].MemberIDmember1.MemberName)
#            members.append(member1.MemberName)
            members.append(member1)

        if g.DEBUG_OL >= 2:
            print(members[0].MemberName, members[0].MemberID,members[0].MemberEmail,members[0].MemberAlias)
            print(members[1].MemberName, members[1].MemberID,members[1].MemberEmail,members[1].MemberAlias)
            
        return(members)
#        for i in range(len(member1)):
#            print(member1[i])
#            members=member1[i][1]
#        print(members)
#        return(members)


# In[ ]:


#query_members_by_team('Sprinters')


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


# ## list_members_page(page,teamid=None)

# In[40]:


def list_members_page(page,teamid=None):
    if g.DEBUG_OL >= 1:
        print('--- function: list_members_page(',page,teamid,')')
    members=[]
    member2=[]
    if teamid == None:
        members = Members.objects(Archived=False).paginate(page,5)
    else:
        membersid=LinkMemberTeam.objects(TeamID=teamid)
        for member in membersid:
            if g.DEBUG_OL >= 2:
                print(member.MemberID)
            memberid,name,firstname,email,theme,project,projectid,team,role,admin,firstcon=query_member_alias(member.MemberID)
            member2=[memberid,name,firstname,email,theme,project,projectid,team,role,admin,firstcon]
            if g.DEBUG_OL >= 2:
                print(member2)
            members.append(member2)
    
    if g.DEBUG_OL >= 2:
            print(members)
    return members


# In[41]:


list_members_page(1,2)


# In[ ]:


print(os.getcwd(),__name__,'imported')

