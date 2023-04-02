#!/usr/bin/env python
# coding: utf-8

# # backend_PI_Roles

# ## prerequisites

# In[ ]:


import global_variables as g
g.init()
import bcrypt
import os
from backend_PI import * # Import tout ce qui est spécifique au projet
from frontend_PI import *
from datetime import datetime

if g.DEBUG_OL == -1:
    print("Debug mode active level :",g.DEBUG_OL)


# In[ ]:


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


# ## archive_status_role(roleid,newstatus)

# In[ ]:


def archive_status_role(roleid,newstatus):
    if g.DEBUG_OL >= 1:
        print('--- function: archive_status_role(',roleid,newstatus,')')
    now = datetime.now()
    role1=Roles.objects(RoleID=roleid).first()
    role1.Archived = newstatus
    role1.LastUpdate = now.strftime("%d/%m/%Y %H:%M:%S")
    role1.save()


# In[ ]:


#archive_status_role(1,False)


# In[ ]:


print(os.getcwd(),__name__,'imported')

