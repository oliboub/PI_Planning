#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Roles

# ## prerequisites

# In[ ]:


import global_variables as g
g.init()
import bcrypt
import os
from mongoengine import *
from backend_PI_mongo_model import *
from datetime import datetime

connect('PIPlanning')
if g.DEBUG_OL == -1:
    print("Debug mode active level :",g.DEBUG_OL)


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


# In[ ]:




