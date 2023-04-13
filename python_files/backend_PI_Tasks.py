#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Tasks

# ## Prerequisites

# ### Imports

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
# - familyid (Epic, Objective,Feature, Sroty, defect)
# - description (not mandatory , but necessary)
# '''

# In[23]:


### Tasks
def create_task(name,memberid,weight,sprintid=None,categoryid=None,familyid=4,description="Thanks to describe your task please'"):
    if g.DEBUG_OL >= 1:    
        print('fonction: create_task(',name,memberid,weight,sprintid,categoryid,familyid,')')
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    task1=Tasks()
    task1.TaskStatusID = 1
    task1.TaskCategoryID = 1
    task1.TaskFamilyID = familyid
    task1.SprintID = 0
    if sprintid != None:
        task1.SprintID = sprintid
        task1.TaskStatusID = 2
        if categoryid != None:
            task1.TaskCategoryID = categoryid
    task1.TaskName = name
    task1.MemberID = memberid
    task1.TaskWeight = weight
    task1.TaskProgress = 0
    task1.CreatedByID = memberid
    task1.CreationDate = creationdate
    task1.UpdatedByID = memberid
    task1.LastUpdate = creationdate
    task1.save()
    
    taskid=task1.TaskID
    if g.DEBUG_OL >= 2:  
        print('task1.TaskID',taskid)

    desc1=TasksDescription()
    desc1.TaskDescription=description
    desc1.CreatedByID = memberid
    desc1.CreationDate=creationdate
    desc1.UpdatedByID = memberid
    desc1.LastUpdate=creationdate
    desc1.save()
    
    descid=desc1.TaskDescriptionID
    if g.DEBUG_OL >= 2:  
        print('desc1.TaskDescriptionID',descid)

    link1=TasksDescriptionLink()
    link1.TaskID=taskid
    link1.TaskDescriptionID=descid
    link1.CreatedByID = memberid
    link1.CreationDate=creationdate
    link1.UpdatedByID = memberid
    link1.LastUpdate=creationdate
    link1.save()

    if g.DEBUG_OL >= 2:  
        print('link1.TaskDescriptionLinkID',link1.TaskDescriptionLinkID)


# In[24]:


#create_task('Create menu to create a task',1,10,None,None,0,description="Thanks to describe your task please'")


# In[49]:


#create_task(name,memberid,weight,sprintid=None,categoryid=None,familyid=0,description="Thanks to describe your task please'")

#create_task('tache pour tester les taches',1,2,1,2,4,'ceci est la description de la tache')
#create_task("d'office pas trop top",1,1.5,2,1)
#create_task("faire le menu pour affichage des tasks",2,2.3,1,3)


# In[9]:


#create_task("essayer d'avancer sur les taches",2,2.3)
#create_task("Penser à deviner la matrice",2,2.3)
#create_task("Remove category of tasks, like the category is linked to the team activity",3,2.3,5)


# ## Add task description

# '''
# in case the lifecycle of a task, we need to add information time to time
# this function allows to add a description to a task with creation date
# inputs:
# - taskID
# - Description
# '''

# In[5]:


def add_task_description(taskid,description,memberid):
    if g.DEBUG_OL >= 1:    
        print('fonction: add_task_description(',taskid,description,memberid,')')
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    desc1=TasksDescription()
    desc1.TaskDescription=description
    desc1.CreatedByID = memberid
    desc1.CreationDate=creationdate
    desc1.UpdatedByID = memberid
    desc1.LastUpdate=creationdate
    desc1.save()

    descid=desc1.TaskDescriptionID
    if g.DEBUG_OL >= 2:  
        print('desc1.TaskDescriptionID',descid) 
        
    link1=TasksDescriptionLink()
    link1.TaskID=taskid
    link1.TaskDescriptionID=descid
    link1.CreatedByID = memberid
    link1.CreationDate=creationdate
    link1.UpdatedByID = memberid
    link1.LastUpdate=creationdate
    link1.save()
    if g.DEBUG_OL >= 2: 
        print('taskid',taskid,'\tdescid',descid,'\tlinkid',link1.TaskDescriptionLinkID)


# In[6]:


#add_task_description(2,"** et encore, je ne t'ai pas tout dit",1)
#add_task_description(1,"Je pense qu'il faudrait discuter avec le BO sur le cas de figure",2)


# In[10]:


#add_task_description(8,'Il ne faut pas faire attendre le mammouth')


# ## list_tasks(memberid,projectin=None,teamin=None,piidin=None,sprintid=None)

# '''
# Can be selected with different variables alone or cumulated:
# - ProjectID
# - PiID
# - SprintID
# '''

# In[97]:


def list_tasks(memberid,projectin=None,teamin=None,piidin=None,sprintid=None):
    if g.DEBUG_OL >= 1:    
        print('fonction: list_tasks(',memberid,projectin,teamin,piidin,sprintid,')')
    if sprintid == None:
        task = Tasks.objects(Archived=False,TaskStatusID=1)
    else:
        task = Tasks.objects(Archived=False,SprintID=sprintid)

#    print('Team\t\t - \t Project')
    task1= []
    desc1 = []
    list_of_tasks=[]
    list_descs=[]

    for task1 in task:
        if g.DEBUG_OL >= 1:    
            print('\n--------------------------')
            print('taskid:',task1.TaskID,'name:',task1.TaskName,'memberid:',task1.MemberID,'weight:',task1.TaskWeight,'progress:',task1.TaskProgress,'sprintid:',task1.SprintID,'statusid:',task1.TaskStatusID,'categoryid',task1.TaskCategoryID)

#get sprint
        piid1 = None
        sprint1 =[]
        
        if task1.SprintID == None or task1.SprintID == 0:
            sprint=None
            piid1=None
            
        else:
            sprint1=Sprints.objects(Archived=False,SprintID=task1.SprintID).first()
            piid1=sprint1.PiID
            if sprint1.SprintSeq != None: 
                sprint=sprint1.SprintSeq
            if g.DEBUG_OL >= 1:   
                print('Sprint Start Date:',sprint1.SprintStartDate,'\tSprint1 Duration:','\tSprint Days:',sprint1.SprintDays,'\tpiid',piid1,'\tsprint:',sprint)

#get taskname
        taskname=task1.TaskName
        taskid=task1.TaskID
# get sprintid
#        sprint=task1.SprintID
    
# get weight
        weight=task1.TaskWeight
        progress=task1.TaskProgress
    
## get member
        member1= Members.objects(MemberID=task1.MemberID).first()
        member=member1.MemberAlias
        
## get team        
        teaml=LinkMemberTeam.objects(MemberID=task1.MemberID).first()
        teami=Teams.objects(TeamID=teaml.TeamID).first()
        team=teami.TeamName

## get status
        status1=TasksStatus.objects(TaskStatusID=task1.TaskStatusID).first()
        status=status1.TaskStatusName

## get piid
        if piid1 != None:

        ## get project
            projecti=Projects.objects(ProjectID=teami.TeamID).first()
            project=projecti.ProjectName
        ## get piid
            piid2=PiPlan.objects(PiID=piid1).first()
            piid=piid2.PiNumber
        else:
            piid=None
            project=None
            
## get category
        categ1=TasksCategory.objects(TaskCategoryID=task1.TaskCategoryID).first()
        category=categ1.TaskCategoryName

## get category
        famil1=TasksFamily.objects(TaskFamilyID=task1.TaskFamilyID).first()
        family=famil1.TaskFamilyName
        
        
## get Result
        if g.DEBUG_OL >= 1:   
            print('taskid:',taskid,'- Task name:',taskname,'\tProject:',project,'- Teamname:',team,'- Member:',member,'\tPI:',piid,'- Sprint:',sprint,'\tTask Weight:',weight,'- Task progress',progress,'- Status:',status,'\tCategory:',category,'- Family:',family)
        detail_tasks=[taskid,taskname,project,team,member,piid,sprint,weight,progress,status,category,family]
        list_of_tasks.append(detail_tasks)
        
    return(list_of_tasks)


# In[99]:


#list_tasks(memberid,projectin=None,teamin=None,piidin=None,sprintid=None):

#list_tasks(1,None,None,None,None)
#list_tasks(1,None,None,None,1)
#list_tasks(1,None,1,1,1)



# In[ ]:


## def list_descriptions()

# def list_descriptions(memberid,projectin=None,teamin=None,piidin=None,sprintid=None):
            desclink=TasksDescriptionLink.objects(TaskID=task1.TaskID)
        desc1 = []
        if desclink != None:
#            print(len(desclink))
            for i in desclink:
                if g.DEBUG_OL >= 1:   
                    print('desclink.TaskID',i.TaskID,'\desclink.TaskDescriptionID',i.TaskDescriptionID)
                desc=TasksDescription.objects(TaskDescriptionID=i.TaskDescriptionID).first()
                if g.DEBUG_OL >= 1:   
                    print('Description:',desc.TaskDescription,'\tLast update:',desc.LastUpdate)
                desclist = [desc.TaskDescription,desc.LastUpdate]
                desc1.append(desclist)
        else:
            if g.DEBUG_OL >= 1:   
                print('None')

#       print(projectin,project,teamin,team,piid,piidin)
    
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

    
    
# In[12]:


if g.DEBUG_OL >= 1:
    print(os.getcwd(),__name__,'imported') 

