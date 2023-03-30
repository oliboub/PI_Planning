#import bcrypt
from mongoengine import *
from backend_PI_mongo_model import *
import os
from datetime import datetime


### Projects
def create_project(project, description):
    print('fonction: create_project(project,description)')
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    proj1=Projects()
    proj1.ProjectName = project
    proj1.ProjectDescription = description
    proj1.CreationDate = creationdate
    proj1.LastUpdate = creationdate
    proj1.save()


def query_project(project):
    print('fonction: query_project(project)')
    project = Projects.objects(ProjectName=project).first()
    return project

def list_projects():
    print('fonction: list_projects()')
    projects = Projects.objects(Archived=False)
    return projects

def query_project_name_from_ID(ID):
    print('fonction: query_project_name_from_ID(ID)')
    project1 = Projects.objects(ProjectID=ID).first()
    return project1

def archive_project(ID):
    print('fonction: archive_project(ID)')
    project1 = Projects.objects(ProjectID=ID).first()
    print('archive_project(ID) fonction:',project1.ProjectName)
    project1.Archived = True
    project1.save()

    
print(os.getcwd(),__name__,'imported')
### ------------------------------

