#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Teams

# ## Prerequisites

# In[2]:


import os
import bcrypt
from datetime import datetime
import PySimpleGUI as sg
from backend_PI_Utils import * # Import tout ce qui est spécifique au projet
from backend_PI_mongo_model import * # Import tout ce qui est spécifique au projet


# In[3]:


import global_variables as g
g.init()
connect('PIPlanning')


# ## create_team(projectID, team, description, logo,memberid)

# In[13]:


def create_team(projectID, newteam, description, logo,memberid):
    if g.DEBUG_OL >= 1:
        print('--- function: create_team(',projectID,',',newteam,',',description,',',logo,',',memberid,')')
    newteam = newteam.capitalize()
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    team1=Teams()
    team1.ProjectID = projectID
    team1.TeamName = newteam
    team1.TeamDescription = description
    team1.TeamLogo = logo
    team1.CreatedByID = memberid
    team1.CreationDate = creationdate
    team1.UpdatedByID = memberid
    team1.LastUpdate = creationdate
    team1.save()

    createdteam=Teams.objects(TeamName=newteam).first()
    if g.DEBUG_OL >= 2:
        print('New team created with TeamID=',createdteam.TeamID)
    
    return createdteam.TeamID


# In[ ]:


#create_team(1, 'Absolut','The best of drinking','../imagesDB/absolut_vodka.jpg')


# # archive_team(teamid,newstatus,memberid)

# In[ ]:


def archive_team(teamid,newstatus,memberid):
    if g.DEBUG_OL >= 1:
        print('--- function: archive_team(',teamid,newstatus,memberid,')')
    item=Teams.objects(TeamID=teamid).first()
    if g.DEBUG_OL >= 2:
        print('archive team name:',item.TeamName)
    now = datetime.now()
    item.Archived = newstatus
    item.UpdatedByID = memberid
    item.LastUpdate = now.strftime("%d/%m/%Y %H:%M:%S")
    item.save()


# ## update_team(projectid,teamid,teamname,teamdescription,teamlogo,memberid)

# In[ ]:


def update_team(projectid,teamid,teamname,teamdescription,teamlogo,memberid):
    if g.DEBUG_OL >= 1:
        print('--- function: update_team(',projectid,teamid,teamname,teamdescription,teamlogo,memberid,')')
    now = datetime.now()
    item=Teams.objects(TeamID=teamid).first()
    item.TeamName = teamname
    item.TeamDescription = teamdescription
    item.ProjectID = projectid
    item.UpdatedByID = memberid
    item.LastUpdate = now.strftime("%d/%m/%Y %H:%M:%S")
    item.save()


# ## update_team_logo(teamid,teamlogo)

# In[1]:


def update_team_logo(teamid,teamlogo):
    if g.DEBUG_OL >= 1:
        print('--- function: update_team_logo(',teamid,teamlogo,')')
    now = datetime.now()
    item=Teams.objects(TeamID=teamid).first()
    item.TeamLogo = teamlogo
    item.LastUpdate = now.strftime("%d/%m/%Y %H:%M:%S")
    item.save()


# ## list_teams(project=None)
# 
# Project can be:
# - **None** for all projects 'Dfefault'
# - **projectID**
# - **ProjectName**

# In[10]:


def list_teams(project=None):
    if g.DEBUG_OL >= 1:
        print('--- function: list_teams(',project,')')
#        print(type(project))
    if project ==  None:
        team = Teams.objects()
    else:
        if type(project) is int:
            pid=project
        else:
            project = project.capitalize()
            projectinfo=Projects.objects(ProjectName=project).first()
            pid=projectinfo.ProjectID
        team = Teams.objects(ProjectID=pid)
        if g.DEBUG_OL >= 2:
            print('Team\t\t - \t Project')
    team1= []
    list_teams=[]
    for team1 in team:
        projectname = Projects.objects(ProjectID=team1.ProjectID).first()
        if projectname is None:
            projectname='Non allocated'
        if team1.TeamLogo != None:
            photo=team1.TeamLogo
        else:
            photo ='../imagesDB/ilovemycompany.jpeg'

        
        if g.DEBUG_OL >= 2:
            print("ProjectID:",team1.ProjectID,"\tProjectName:",projectname.ProjectName,"\tTeamID:",team1.TeamID,'\tTeamName:',team1.TeamName,'\tlogo:',photo,'\tlastupdate:',team1.LastUpdate,'\tArchived:',team1.Archived)
        teams=[team1.ProjectID,projectname.ProjectName,team1.TeamID,team1.TeamName,team1.TeamDescription,photo,team1.LastUpdate,team1.Archived]
        list_teams.append(teams)
#    if g.DEBUG_OL >= 2:
#        for i in list_teams:
#            print(i)
#    print(list_teams[0][1])
    return(list_teams)


# In[12]:


#list_teams("titi")


# In[ ]:


if g.DEBUG_OL >= 1:
    print(os.getcwd(),__name__,'imported')

