#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Roles

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


# ## create_role(role,description)

# In[ ]:


def create_role(newrole,description):
    if g.DEBUG_OL >= 1:
        print('--- function: create_role(',newrole,description,')')
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    role = Roles()
    role.RoleName =  newrole
    role.RoleDescription = description
    role.Archived=False
    role.CreationDate = creationdate
    role.LastUpdate = creationdate
    role.save()
    
    createdrole=Roles.objects(RoleName=newrole).first()
    if g.DEBUG_OL >= 2:
        print('New role created with roleID=',createdrole.RoleID)
    
    return createdrole.RoleID


# In[ ]:


#create_role("Busines Owner","Business owner for SAP HR")


# ## archive_role(roleid,newstatus)

# In[ ]:


def archive_role(roleid,newstatus):
    if g.DEBUG_OL >= 1:
        print('--- function: archive_role(',roleid,newstatus,')')
    now = datetime.now()
    role1=Roles.objects(RoleID=roleid).first()
    role1.Archived = newstatus
    role1.LastUpdate = now.strftime("%d/%m/%Y %H:%M:%S")
    role1.save()


# In[ ]:


#archive_status_role(1,False)


# ## update_role(roleid,rolename,roledescription)

# In[ ]:


def update_role(roleid,rolename,roledescription):
    if g.DEBUG_OL >= 1:
        print('--- function: update_role(',roleid,rolename,roledescription,')')
    now = datetime.now()
    role1=Roles.objects(RoleID=roleid).first()
    role1.RoleName = rolename
    role1.RoleDescription = roledescription
    role1.LastUpdate = now.strftime("%d/%m/%Y %H:%M:%S")
    role1.save()


# In[ ]:


print(os.getcwd(),__name__,'imported')

