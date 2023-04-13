#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import bcrypt
from mongoengine import *
#from mongoengine_pagination import DocumentPro


# In[ ]:


class Projects(Document):
#    id = SequenceField(primary_key=True)
    ProjectID = SequenceField()      # IDentifiant du projet
    ProjectName = StringField(required=True, unique=True) # Nom du projet]
    ProjectDescription = StringField() # Description du projet]
    ProjectPIPlanning = DateField()                       # Date du PI Planning
    ProjectPIPlanningDuration = IntField(default=2)       # Durée du PI Planning
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # Project archived
    
class Teams(Document):
#    id = SequenceField(primary_key=True)
    TeamID = SequenceField()          # ID de l'équipe
    TeamName = StringField(required=True, unique=True)    # Nom de l'équipe
    TeamDescription = StringField()                       # Explicaiton du role de l'équipe
#    PiID = IntField()                        # identifiant du PI, sera rentré au moment de la création du PI planning
    ProjectID = IntField()                        # identifiant du Project
    TeamLogo = StringField()    # logo de l'équipe
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # Teams archived

hashAndSalt = bcrypt.hashpw('default1234'.encode(), bcrypt.gensalt())
class Members(Document):
#    id = SequenceField(primary_key=True)
    MemberID = SequenceField()  # Identifiant de la personne
    MemberName =  StringField(required=True)
    MemberFirstName = StringField(required=True)
    MemberEmail = EmailField(required=True,unique=True)
    MemberAlias = StringField(required=True, unique=True)
    MemberRole = IntField(required=True) # Role de la personne
    MemberTheme = StringField() # Theme pour l'interface utilisateur
    MemberAvatar = StringField()
    MemberPassword = BinaryField(default=hashAndSalt)
    MemberFirstConnection = BooleanField(default=True)
    MemberAdmin = BooleanField(default=False)
    MemberPortfolio = BooleanField(default=False)
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # Membres actifs
    
class Sprints(Document):
#    id = SequenceField(primary_key=True)
    SprintID = SequenceField()       # IDentifiant du projet
    PiID = IntField(required=True) # Identifiant du PI
    SprintSeq = IntField(required=True) # sprints number
    SprintDays = IntField() # Nombre de jours du sprint
    SprintStartDate = DateField() # Date du Sprint1
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived=BooleanField(default=False)     

class PiPlan(Document):
#    id = SequenceField(primary_key=True)
    PiID = SequenceField()  # Identifiant du PI
    ProjectID = IntField(required=True)      # IDentifiant du projet
    PiCurrent = BooleanField(default=False) # PI en cours
    PiNumber = IntField(required=True)      # Project PI number
    PiTeams = IntField(required=True,defaul=1)       # Nombre d'équipes agiles du projet
    PiSprintWeeks = IntField(required=True) # Nombre de semaines par sprint
    PiSprintQtt = IntField(required=True)  # Nombre de sprints
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # PI archived

#class User(Document):
#    username = StringField(required=True, unique=True)
#    password = BinaryField(required=True)
#    email = EmailField(required=True, unique=True)
#    DefaultProject = IntField(default=0)
#    CreatedByID=IntField()
#    CreationDate = DateTimeField()
#    UpdatedByID=IntField()
#    LastUpdate = DateTimeField()
#    Archived = BooleanField(default=False) # PI archived

class Roles(Document):
    RoleID = SequenceField()  # identifiant unique
    RoleName = StringField(required=True, unique=True)
    RoleDescription = StringField()
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # PI archived

# Tables de liens
class LinkMemberTeam(Document):
#    id = SequenceField(primary_key=True)
    LinkMemberTeamID = SequenceField()  # IDentifiant de l'alocation
    MemberID = IntField(required=True) # Identifiant de la personne
    TeamID = IntField(required=True) # identifiant de lequipe
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # PI archived

class Piteams(Document):
    PiTeamsID = SequenceField()  # identifiant unique de capacity
    PiID = IntField(required=True)
    TeamID = IntField(required=True)
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # PI archived

class Capacity(Document):
#    id = SequenceField(primary_key=True)
    CapacityID = SequenceField()  # identifiant unique de capacity
    SprintID = IntField(required=True)
    MemberID = IntField(required=True)
    CapacityDays = IntField(required=True)
    MissingDays = IntField(default=0)
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # PI archived

#class LinkMemberRole(Document):
#    LinkMemberRoleID = SequenceField()  # identifiant unique
#    MemberID =  IntField(required=True)
#    RoleID =  IntField(required=True)


#### Tasks 

class Tasks(Document):
    TaskID = SequenceField()
    SprintID = IntField()
    TaskFamilyID = IntField(required=True,default=1)
    TaskCategoryID = IntField(required=True,default=5)
    TaskName = StringField(required=True)
    TaskWeight=FloatField()
    TaskProgress=FloatField(min_value=0, max_value=1)
    TaskStatusID=IntField(required=True,default=5)
    MemberID=IntField()
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False)
    
class TasksDependency(Document):
    TaskDepencyID=SequenceField()
    TaskIDS=IntField(required=True) # Source
    TaskIDT=IntField(required=True) # Target
    TaskDepencyCategoryID=IntField(required=True) # Category od dependency
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # PI archived

class TasksDependencyCategory(Document):
    TaskDepencyCategoryID=SequenceField()
    TaskDependencyCategoryName=StringField(required=True)
    TaskDependencyCategoryDescription=StringField()
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # PI archived
    
class TasksDescriptionLink(Document):
    TaskDescriptionLinkID=SequenceField()
    TaskID=IntField(required=True)
    TaskDescriptionID=IntField(required=True)
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # PI archived

class TasksDescription(Document):
    TaskDescriptionID=SequenceField()
    TaskDescription=StringField()
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # PI archived

class TasksCategory(Document):
    TaskCategoryID = SequenceField()
    TaskCategoryProjectID = IntField(required=True)
    TaskCategoryName = StringField(required=True)
    TaskCategoryDescription = StringField()
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # PI archived

class TasksFamily(Document):
    TaskFamilyID = SequenceField()
    TaskFamilyName = StringField(required=True)
    TaskFamilyDescription = StringField()
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # PI archived
    

class TasksStatus(Document):
    TaskStatusID=SequenceField()
    TaskStatusName=StringField(required=True)
    TaskStatusDescription=StringField()
    CreatedByID=IntField()
    CreationDate = DateTimeField()
    UpdatedByID=IntField()
    LastUpdate = DateTimeField()
    Archived = BooleanField(default=False) # PI archived


# In[ ]:


#if g.DEBUG_OL >= 1:
print(os.getcwd(),__name__,'imported')


# In[ ]:




