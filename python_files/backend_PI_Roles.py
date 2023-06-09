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


# ## create_role(role,description,memberid)

# In[ ]:


def create_role(newrole,description,memberid):
    if g.DEBUG_OL >= 1:
        print('--- function: create_role(',newrole,description,memberid,')')
    newrole=newrole.title()
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    role = Roles()
    role.RoleName =  newrole
    role.RoleDescription = description
    role.Archived=False
    role.CreatedByID = memberid
    role.CreationDate = creationdate
    role.UpdatedByID = memberid
    role.LastUpdate = creationdate
    role.save()
    
    createdrole=Roles.objects(RoleName=newrole).first()
    if g.DEBUG_OL >= 2:
        print('New role created with roleID=',createdrole.RoleID)
    
    return createdrole.RoleID


# In[ ]:


#create_role("busines owner HR","Business owner for SAP HR")


# ## archive_role(roleid,newstatus,memberid)

# In[ ]:


def archive_role(roleid,newstatus,memberid):
    if g.DEBUG_OL >= 1:
        print('--- function: archive_role(',roleid,newstatus,memberid,')')
    item=Roles.objects(RoleID=roleid).first()
    if g.DEBUG_OL >= 2:
        print('archive role name:',item.RoleName)
    now = datetime.now()
    item.Archived = newstatus
    item.UpdatedByID = memberid
    item.LastUpdate = now.strftime("%d/%m/%Y %H:%M:%S")
    item.save()


# In[ ]:


#archive_status_role(1,False)


# ## update_role(roleid,rolename,roledescription,memberid)

# In[ ]:


def update_role(roleid,rolename,roledescription,memberid):
    if g.DEBUG_OL >= 1:
        print('--- function: update_role(',roleid,rolename,roledescription,memberid,')')
    now = datetime.now()
    item=Roles.objects(RoleID=roleid).first()
    item.RoleName = rolename
    item.RoleDescription = roledescription
    item.UpdatedByID = memberid
    item.LastUpdate = now.strftime("%d/%m/%Y %H:%M:%S")
    item.save()


# In[ ]:


if g.DEBUG_OL >= 1:
    print(os.getcwd(),__name__,'imported')

