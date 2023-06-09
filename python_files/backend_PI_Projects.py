#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Projects

# ## prerequisites

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


# ## create_project(project, description)

# In[ ]:


def create_project(project, description,memberid):
    if g.DEBUG_OL >= 1:
        print('function: create_project',project,description,memberid,')')
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    item=Projects()
    item.ProjectName = project
    item.ProjectDescription = description
    item.CreatedByID = memberid
    item.CreationDate = creationdate
    item.UpdatedByID = memberid
    item.LastUpdate = creationdate
    item.save()

    createdproject=Projects.objects(ProjectName=project).first()
    if g.DEBUG_OL >= 2:
        print('New project created with projectID=',createdproject.ProjectID)
    
    return createdproject.ProjectID


# In[ ]:


#create_project('Guerre du Nord', 'Guerre virtuelle qui se passe dans les pays froid')


# ## list_projects(project=None)
# project might be:
# - projecid
# - projectname
# - None (for all)

# In[ ]:


def list_projects(project=None):
    if g.DEBUG_OL >= 1:
        print('--- function: list_projects(',project,')')
    if project ==  None:
        projects = Projects.objects()
    else:
        if type(project) is int:
            pid=project
        else:
            projectinfo=Projects.objects(ProjectName=project).first()
            pid=projectinfo.ProjectID
        projects = Projects.objects(ProjectID=pid)
    if g.DEBUG_OL >= 2:
        for i in projects:
            print("project:",i.ProjectName, '\tProjectID:',i.ProjectID, '\tProjectDescription',i.ProjectDescription,'\tProjectStatus',i.Archived)
        
    return(projects)


# In[ ]:


# list_projects(1)


# ## archive_project(projectid,newstatus,memberid)

# In[ ]:


def archive_project(projectid,newstatus,memberid):
    if g.DEBUG_OL >= 1:
        print('function: archive_project(',projectid,newstatus,memberid,')')
    item = Projects.objects(ProjectID=projectid).first()
    if g.DEBUG_OL >= 2:
        print('archive_project name:',item.ProjectName)
    now = datetime.now()
    item.Archived = newstatus
    item.UpdatedByID = memberid
    item.LastUpdate = now.strftime("%d/%m/%Y %H:%M:%S")
    item.save()


# In[ ]:


#archive_project(2,False)


# ## update_project(projectid,projectname,projectdescription,memberid)

# In[ ]:


def update_project(projectid,projectname,projectdescription,memberid):
    if g.DEBUG_OL >= 1:
        print('--- function: update_role(',projectid,projectname,projectdescription,memberid,')')
    now = datetime.now()
    item=Projects.objects(ProjectID=projectid).first()
    item.ProjectName = projectname
    item.ProjectDescription = projectdescription
    item.UpdatedByID = memberid
    item.LastUpdate = now.strftime("%d/%m/%Y %H:%M:%S")
    item.save()


# In[ ]:


#update_project(4,'Guerre du Nord',"Guerre qui démarre au Nord")
#update_project(4,'Guerre du Sud',"Guerre qui s'est déplacée au sud")


# In[ ]:


if g.DEBUG_OL >= 1:
    print(os.getcwd(),__name__,'imported')

