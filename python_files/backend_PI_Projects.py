#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Projects

# ## prerequisites

# In[ ]:


#import bcrypt
import os
from backend_PI import * # Import tout ce qui est spécifique au projet
from frontend_PI import *
from datetime import datetime

connect('PIPlanning')


# ## create_project(project, description)

# In[ ]:


def create_project(project, description):
    if g.DEBUG_OL >= 1:
        print('fonction: create_project',project,description,')')
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    proj1=Projects()
    proj1.ProjectName = project
    proj1.ProjectDescription = description
    proj1.CreationDate = creationdate
    proj1.LastUpdate = creationdate
    proj1.save()


# ## query_project(project)

# In[ ]:


def query_project(project):
    if g.DEBUG_OL >= 1:
        print('fonction: query_project(',project,')')
    project = Projects.objects(ProjectName=project).first()
    return project


# ## list_projects()

# In[ ]:


def list_projects():
    if g.DEBUG_OL >= 1:
        print('fonction: list_projects()')
    projects = Projects.objects(Archived=False)
    return projects


# ## query_project_name_from_ID(ID

# In[ ]:


def query_project_name_from_ID(ID):
    if g.DEBUG_OL >= 1:
        print('fonction: query_project_name_from_ID(',ID,')')
    project = Projects.objects(ProjectID=ID).first()
    return project


# ## archive_project(ID)

# In[ ]:


def archive_project(ID):
    if g.DEBUG_OL >= 1:
        print('fonction: archive_project(',ID,')')
    project1 = Projects.objects(ProjectID=ID).first()
    if g.DEBUG_OL >= 2:
        print('archive_project(ID) fonction:',project1.ProjectName)
    project1.Archived = True
    project1.save()


# In[ ]:


print(os.getcwd(),__name__,'imported')


# In[ ]:




