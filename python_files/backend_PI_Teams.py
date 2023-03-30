#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Teams

# ## Prerequisites

# In[1]:


import global_variables as g
g.init()
import bcrypt
import os
from mongoengine import *
from backend_PI_mongo_model import *
from datetime import datetime

connect('PIPlanning')


# ## create_team(projectID, team, description, logo)

# In[ ]:


def create_team(projectID, team, description, logo):
    if g.DEBUG_OL >= 1:
        print('--- function: create_team(',projectID,',',team,',',description,',',logo,')')
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    team1=Teams()
    team1.ProjectID = projectID
    team1.TeamName = team
    team1.TeamDescription = description
    team1.TeamLogo = logo
    team1.CreationDate = creationdate
    team1.LastUpdate = creationdate
    team1.save()


# In[ ]:


# test


# ## list_teams(project=None)
# 
# Project can be:
# - **None** for all projects 'Dfefault'
# - **projectID**
# - **ProjectName**

# In[25]:


def list_teams(project=None):
    if g.DEBUG_OL >= 1:
        print('--- function: list_teams_all(',project,')')
        print(type(project))
    if project ==  None:
        team = Teams.objects(Archived=False)
    else:
        if type(project) is int:
            pid=project
        else:
            projectinfo=Projects.objects(ProjectName=project).first()
            pid=projectinfo.ProjectID
        team = Teams.objects(Archived=False,ProjectID=pid)
        if g.DEBUG_OL >= 2:
            print('Team\t\t - \t Project')
    team1= []
    list_teams=[]
    for team1 in team:
        projectname = Projects.objects(ProjectID=team1.ProjectID).first()
        if projectname is None:
            projectname='Non allocated'
        if g.DEBUG_OL >= 2:
            print("ProjectName:",projectname.ProjectName,"\tProjectID:",team1.ProjectID,"\tTeamID:",team1.TeamID)
        teams=[projectname.ProjectName,team1.TeamName,team1.TeamDescription,team1.TeamLogo]
        list_teams.append(teams)
#    if g.DEBUG_OL >= 2:
#        for i in list_teams:
#            print(i)
#    print(list_teams[0][1])
    return(list_teams)


# In[26]:


#list_teams_all("titi")


# ## list_teams_page(page,projectid=None)

# In[2]:


def list_teams_page(page,projectid=None):
    if g.DEBUG_OL >= 1:
        print('--- function: list_teams_page(',page,projectid,')')
    if projectid == None:
        teams = Teams.objects(Archived=False).paginate(page,5)
    else:
        teams = Teams.objects(ProjectID=projectid,Archived=False).paginate(page,5)
           
    if g.DEBUG_OL >= 2:
        for a in teams.items:
            print(a.TeamName,'\t',a.TeamDescription,'\t',a.TeamLogo,'\t',a.ProjectID)
    return teams


# In[3]:


#list_teams_page(1,1)


# In[ ]:


print(os.getcwd(),__name__,'imported')

