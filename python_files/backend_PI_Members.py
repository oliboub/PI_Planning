#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Members

# ## prerequisites

# In[1]:


import bcrypt
from mongoengine import *
from backend_PI_mongo_model import *
from datetime import datetime

connect('PIPlanning')


# ## query_members_alias(alias)

# In[1]:


#
### members
def query_member_alias(Alias):
    print('fonction: query_member_alias(',Alias,')')
    try:
        member1 = Members.objects(Archived=False,MemberAlias=Alias).first()
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
    if debug_ol == 1:
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
        
    
    return(member1.MemberID,member1.MemberName,member1.MemberFirstName,member1.MemberEmail,member1.MemberTheme,project.ProjectName,team.TeamName,role.RoleName,member1.MemberAdmin,member1.MemberFirstConnection)


# In[15]:


#query_member_alias('superadmin')


# ## query_members_by_team

# In[4]:


def query_members_by_team(teamname='All'):
    print('fonction: query_members_by_team(',teamname,')')
    members = []
    if teamname is None:
        print('Please add a teamname as parameter')
        return('[]')

    else:
        if teamname != 'All':
            teams=Teams.objects(TeamName=teamname).first()
            print(teams)

            if teams is None:
                print("'None' value provided for item of farkling routine")
                return('[]')

            else:
                link=LinkMemberTeam.objects(TeamID=teams.TeamID)
                print(link)
        else:
            link=LinkMemberTeam.objects()
            
        for i in range(len(link)):
#            print(link[i].MemberID)
            member1=Members.objects(MemberID=link[i].MemberID).first()
#            print(member1.MemberName)
            members.append(member1.MemberName)
        print(members)
        return(members)
#        for i in range(len(member1)):
#            print(member1[i])
#            members=member1[i][1]
#        print(members)
#        return(members)


# In[5]:


#query_members_by_team('All')


# ## query_member(alias)

# In[1]:


def query_member(alias):
    print('fonction: query_member(',alias,')')
    if alias.find('@'):
        print('Email')
        member1 = Members.objects(Archived=False,MemberEmail=alias).first()
        if member1 is None:
            print('None')
            return(1,'None')
        else:
            print(member1.MemberName)
            return(0,member1)
        return(0,member1)        
    else:
        print('alias')
        member1 = Members.objects(Archived=False,MemberAlias=alias).first()
        if member1 is None:
            print('None')
            return(1,'None')
        else:
            print(member1.MemberName)
            return(0,member1)


# In[9]:


#query_member('oliboub')


# ## write_new_member_theme(memberid,theme)

# In[ ]:


def write_new_member_theme(memberid,theme):
    print('fonction: write_new_member_theme(',theme,')')
    member1 = Members.objects(MemberID=memberid).first()
    member1.MemberTheme=theme
    member1.save()   


# In[ ]:


## create_member(MemberName,FirstName.Email,MemberTheme)'lightblue2',ProjectName,TeamName,RoleName,admin=False)


# In[3]:


def create_member(name,firstname,alias,email,theme,photo,projectid,teamid,roleid,password="default123",admin=False):
    print('fonction: create_member(',name,firstname,password,alias,email,theme,photo,projectid,teamid,roleid,admin,')')
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


# In[38]:


def update_member_password(email,password):
    print('fonction: update_member_passwd(',email,'password',')',)
    member1 = Members.objects(Archived=False,MemberEmail=email).first()
    debug_ol=0
    if debug_ol == 1:
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
    if debug_ol == 1:
        print('------ After')
        print('MemberID:',member1.MemberID)
        print('User Alias:',member1.MemberAlias)
        print('User Name:',member1.MemberName)
        print('User First Name:',member1.MemberFirstName)
        print('User Email:',member1.MemberEmail)
        print('Member First Connection:',member1.MemberFirstConnection)
        print('Member Last Update:',member1.LastUpdate)
        print('Member Password:',member1.MemberPassword)

    


# In[37]:


#update_member_password('oliboub@gmail.com','aaaaaaaa')


# In[26]:


def get_actual_password(email,passwd):
    print('fonction: get_actual_password(',email,'password)',)
    password=passwd.encode('utf-8')
    strikepwd= bcrypt.hashpw(password, bcrypt.gensalt())
    
    member1 = Members.objects(Archived=False,MemberEmail=email).first()
    debug_ol=0
    if debug_ol == 1:
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
        print("It matches")
        a=True
    else:
        print("It does not match")
        a=False
    return(a)


# In[36]:


#get_actual_password('admin@gmail.com','aaaaaaaa')


# In[19]:


print(__name__,'imported')


# In[ ]:



