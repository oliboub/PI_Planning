#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Tasks

# ## Prerequisites

# ### Imports

# In[ ]:


import os
import bcrypt
from datetime import datetime
import PySimpleGUI as sg
from backend_PI_Utils import * # Import tout ce qui est spécifique au projet
from backend_PI_mongo_model import * # Import tout ce qui est spécifique au projet
#from backend_PI import * # Import tout ce qui est spécifique au projet
#from frontend_PI import *


# In[ ]:


import global_variables as g
g.init()
connect('PIPlanning')


# ## Create Task

# '''
# Ths function intend to create a task linked to a sprint or to the backlog
# Backlog means no sprint, with default not plan and no status
# This create_task also creates the first description.
# 
# Inputs: 
# - Name of task
# - allocated memberID
# - weight of this task in an agile definition
# - sprintID (not mandatory)
# - category (not mandatory) - can be a family of activity in a team
# - description (not mandatory , but necessary)
# '''

# In[4]:


### Tasks
def create_task(name,memberid,weight,sprintid=None,categoryid=None,description="Thanks to describe your task please'"):
    if g.DEBUG_OL >= 1:    
        print('fonction: create_task(',name,memberid,weight,sprintid,categoryid,')')
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    task1=Tasks()
    if sprintid != None:
        task1.SprintID = sprintid
        task1.TaskStatusID = 1
        if categoryid != None:
            task1.TaskCategoryID = categoryid
    task1.TaskName = name
    task1.MemberID = memberid
    task1.TaskWeight = weight
    task1.TaskProgress = 0
    task1.CreationDate = creationdate
    task1.LastUpdate = creationdate
    task1.save()
    taskid=task1.TaskID
    print(taskid)

    desc1=TasksDescription()
    desc1.TaskDescription=description
    desc1.CreationDate=creationdate
    desc1.LastUpdate=creationdate
    desc1.save()
    descid=desc1.TaskDescriptionID
    print(descid)

    link1=TasksDescriptionLink()
    link1.TaskID=taskid
    link1.TaskDescriptionID=descid
    link1.save()
    print(link1.TaskDescriptionLinkID)


# ## Add task description

# '''
# in case the lifecycle of a task, we need to add information time to time
# this function allows to add a description to a task with creation date
# inputs:
# - taskID
# - Description
# '''

# In[6]:


def add_task_description(taskid,description):
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    desc1=TasksDescription()
    desc1.TaskDescription=description
    desc1.CreationDate=creationdate
    desc1.LastUpdate=creationdate
    desc1.save()
    descid=desc1.TaskDescriptionID
 
    link1=TasksDescriptionLink()
    link1.TaskID=taskid
    link1.TaskDescriptionID=descid
    link1.save()
    print('taskid',taskid,'\tdescid',descid,'\tlinkid',link1.TaskDescriptionLinkID)

def task_link_desk(taskid,descid):
    link1=TasksDescriptionLinks()
    link1.TaskID=taskid
    link1.TaskDescriptionID=descid#add_task_description(15,"** et encore, je ne t'ai pas tout dit")
# ## List Task

# '''
# Can be selected with different variables alone or cumulated:
# - ProjectID
# - PiID
# - SprintID
# '''

# In[21]:


def list_tasks(projectin='All',teamin='All',piidin='All',sprintid='All'):
    print('fonction: list_tasks(',projectin,teamin,piidin,sprintid,')')
    if sprintid == 'All':
        task = Tasks.objects(Archived=False)
    elif sprintid == None:
        task = Tasks.objects(Archived=False,TaskCategoryID=5)
    else:
        task = Tasks.objects(Archived=False,SprintID=sprintid)

#    print('Team\t\t - \t Project')
    task1= []
    desc1 = []
    list_tasks=[]
    list_descs=[]

    for task1 in task:
#        print('task1.TaskStatusID',task1.TaskStatusID)
#        print(task1.TaskID,task1.TaskName,task1.MemberID,task1.TaskWeight,task1.TaskProgress,task1.TaskStatusID,task1.TaskCategoryID)

#get sprint
        piid1 = None
        if task1.SprintID !=None:
            sprint1=Sprints.objects(Archived=False,SprintID=task1.SprintID).first()
            piid1=sprint1.PiID
            if sprint1.SprintSeq != None: 
                sprint=sprint1.SprintSeq
        else:
            sprint=None
#        print('Sprint Start Date:',sprint1.SprintStartDate,'\tSprint1 Duration:',sprint1.SprintDays,sprint,piid1)

#get taskname
        taskname=task1.TaskName

# get sprintid
#        sprint=task1.SprintID
    
# get weight
        weight=task1.TaskWeight
    
## get member
        member1= Members.objects(MemberID=task1.MemberID).first()
        member=member1.MemberAlias
## get team        
        teaml=LinkMemberTeam.objects(MemberID=task1.MemberID).first()
        teami=Teams.objects(TeamID=teaml.TeamID).first()
        team=teami.TeamName
## get project
        projecti=Projects.objects(ProjectID=teami.TeamID).first()
        project=projecti.ProjectName

## get status
        status1=TasksStatus.objects(TaskStatusID=task1.TaskStatusID).first()
        status=status1.TaskStatusName

## get piid
        if piid1 != None:
            piid2=PiPlan.objects(PiID=piid1).first()
            piid=piid2.PiNumber
        else:
            piid=None
## get category
        categ1=TasksCategory.objects(TaskCategoryID=task1.TaskCategoryID).first()
        category=categ1.TaskCategoryName
        
## get Descriptions
#        print('\nProject:',project,'\tTeamname:',team,'\tMember:',member,'\tSprint:',sprint,'\tTask name:',taskname,'\tTask Weight:',weight,'\tTask progress',task1.TaskProgress,'\tStatus:',status,'\tCategory:',category)

        desclink=TasksDescriptionLink.objects(TaskID=task1.TaskID)
        desc1 = []
        if desclink != None:
#            print(len(desclink))
            for i in desclink:
 #               print('desclink.TaskID',i.TaskID,'\desclink.TaskDescriptionID',i.TaskDescriptionID)
                desc=TasksDescription.objects(TaskDescriptionID=i.TaskDescriptionID).first()
 #               print('Description:',desc.TaskDescription,'\tLast update:',desc.LastUpdate)
                desclist = [desc.TaskDescription,desc.LastUpdate]
                desc1.append(desclist)
#        else:
#            print('None')
#        print(projectin,project,teamin,team,piid,piidin)
    
        if projectin == 'All' or projectin == project:
            if teamin == 'All' or team == teamin:
                if piidin == 'All' or piidin == piid:
                    task1=[project,team,piid,sprint,member,taskname,weight,task1.TaskProgress,status,category]
                    list_tasks.append(task1)
                    list_descs.append(desc1)
                if piid == None and piidin == None:
                    task1=[project,team,piid,sprint,member,taskname,weight,'None',status,category]
                    list_tasks.append(task1)
                    list_descs.append(desc1)

#       print(task1)
#        print(desc1)
#        list_tasks.append(task1)
#        list_descs.append(desc1)
        
#        if projectname is None:
#            projectname='Non allocated'
#        print(projectname.ProjectName)
#        teams=[projectname.ProjectName,team1.TeamName,team1.TeamDescription,team1.TeamLogo]
#        list_teams.append(teams)
    for i in range(len(list_tasks)):
        print(list_tasks[i])
        for j in range(len(list_descs[i])):
            print(list_descs[i][j])
        print('\n----\n')
#    print(list_teams[0][1])
#    return(list_teams)   


# In[9]:


#create_task(name,memberid,weight,sprintid=None,categoryid=None)
#create_task('Faire un menu différent poru les admins',1,0.9,6,1,'ceci est la description de ouf')
#create_task("d'office pas trop top",1,1.5,2,1)
#create_task("faire le menu pour affichage des tasks",2,2.3,1,3)


# In[25]:


#create_task("essayer d'avancer sur les taches",2,2.3)
#create_task("Penser à deviner la matrice",2,2.3)
#create_task("Remove category of tasks, like the category is linked to the team activity",3,2.3,5)


# add_task_description(8,'Il ne faut pas faire attendre le mammouth')

# In[30]:


#list_tasks(projectin=None,teamin='All',piidin='All',sprintid='All')
#list_tasks('All','PI','All','All')


# In[ ]:


if g.DEBUG_OL >= 1:
    print(os.getcwd(),__name__,'imported') 

