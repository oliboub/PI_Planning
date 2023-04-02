#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Members

# ## prerequisites

# In[ ]:


import global_variables as g
g.init()
import PySimpleGUI as sg
from backend_PI import * # Import tout ce qui est spécifique au projet
from frontend_PI import *
import os


# In[ ]:


connect('PIPlanning')


# ## query_member(alias)

# In[ ]:


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

# In[ ]:


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
#    print(team.TeamID)
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
        print('Project Team ID:',team.TeamID)
        print('Project Team allocated:',team.TeamName)
        print('User Theme:',member1.MemberTheme)
        print('Team Role:',role.RoleName)
        print('Member admin:',member1.MemberAdmin)
        print('Member First Connection:',member1.MemberFirstConnection)
        
    
    return(member1.MemberID,member1.MemberName,member1.MemberAlias,member1.MemberFirstName,member1.MemberEmail,member1.MemberTheme,project.ProjectName,project.ProjectID,team.TeamName,team.TeamID,role.RoleName,member1.MemberAdmin,member1.MemberFirstConnection)


# In[ ]:


#query_member_alias(1)


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

    membersid=[]
    members =[]
    members1=[]
    members2=[]
    member2=[]
    teamid=0
    
    if team == 'All':
        members1 = Members.objects(Archived=False)
        if g.DEBUG_OL >= 2:
            print(len(members1))

    if type(team) is str and team != 'All' :
        try:
            teamselected=Teams.objects(Archived=False,TeamName=team).first()
            teamid=teamselected.TeamID
            if g.DEBUG_OL >= 2:
                print(teamid)
        except Exception as e:
            return "Error: %s" % (e)
            end()
    elif type(team) is int:
        teamid=team
        
    if teamid != 0:
        members1=LinkMemberTeam.objects(TeamID=teamid)

        if g.DEBUG_OL >= 2:
            print('teamid:',teamid,'Qtt members found:',len(members1))      


    for i in members1:
        membersid.append(i.MemberID)
        if g.DEBUG_OL >= 2:
            print(membersid)
        
    for member in membersid:
        if g.DEBUG_OL >= 2:
                print(member)
        memberid,name,alias,firstname,email,theme,project,projectid,team,teamid,role,admin,firstcon=query_member_alias(member)
        member2=[memberid,name,alias,firstname,email,theme,project,projectid,team,teamid,role,admin,firstcon]
        if g.DEBUG_OL >= 2:
            print(member2)
        members.append(member2)
    
    return(members)


# In[ ]:


#query_members_by_team(2)


# ## write_new_member_theme(memberid,theme)

# In[ ]:


def write_new_member_theme(memberid,theme):
    if g.DEBUG_OL >= 1:
        print('--- function: write_new_member_theme(',memberid,theme,')')
    member1 = Members.objects(MemberID=memberid).first()
    member1.MemberTheme=theme
    member1.save() 


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


#create_member('Artic', 'Haud','haudartic','haudartic@toto.com',2,2,'LightBlue2','default123',False )


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

