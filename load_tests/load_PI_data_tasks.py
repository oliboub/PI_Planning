from backend_PI_mongo_model import *
from datetime import datetime


connect('PIPlanning')

now = datetime.now()
 
#print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#print("date and time =", dt_string)


task1 =Tasks()
task1.SprintID = 1
task1.TaskCategoryID = 5
task1.TaskName = "Création d'une collection de logs d'activité"
task1.MemberID=1
task1.TaskWeight=0.6
task1.TaskProgress=0
task1.TaskStatusID=5
task1.CreationDate=dt_string
task1.LastUpdate=dt_string
task1.save()

taskl1 = TasksDescriptionLink()
taskl1.TaskID=1
taskl1.TaskDescriptionID=1
taskl1.save()

taskl2 = TasksDescriptionLink()
taskl2.TaskID=1
taskl2.TaskDescriptionID=2
taskl2.save()

taskl1 = TasksDescriptionLink()
taskl1.TaskID=2
taskl1.TaskDescriptionID=3
taskl1.save()


taskd1 = TasksDescription()
taskd1.TaskDescription="use case: en cas d'audit et de besoin d'analyse, nous devons etre capable de donner toutes les logs d'acivités à un data scientist"
taskd1.CreationDate=dt_string
taskd1.LastUpdate=dt_string
taskd1.save()

taskd2 = TasksDescription()
taskd2.TaskDescription="On essaye de penser data science as concept"
taskd2.CreationDate=dt_string
taskd2.LastUpdate=dt_string
taskd2.save()

taskd3 = TasksDescription()
taskd3.TaskDescription="Encore un peu de detail pour prendre la décision qui s'impose. On a pas tous les jours 20 ans et ça fait mal."
taskd3.CreationDate=dt_string
taskd3.LastUpdate=dt_string
taskd3.save()


taskf1 = TasksFamily()
taskf1.TaskFamilyName = 'Epic'
taskf1.TaskFamilyDescription = 'Link to all Epic'
taskf1.CreationDate=dt_string
taskf1.LastUpdate=dt_string
taskf1.save()

taskf2 = TasksFamily()
taskf2.TaskFamilyName = 'Capability'
taskf2.TaskFamilyDescription = 'Link to all Capabiliy'
taskf2.CreationDate=dt_string
taskf2.LastUpdate=dt_string
taskf2.save()

taskf3 = TasksFamily()
taskf3.TaskFamilyName = 'Feature'
taskf3.TaskFamilyDescription = 'Link to all features'
taskf3.CreationDate=dt_string
taskf3.LastUpdate=dt_string
taskf3.save()

taskf4 = TasksFamily()
taskf4.TaskFamilyName = 'Story'
taskf4.TaskFamilyDescription = 'Link to all Story'
taskf4.CreationDate=dt_string
taskf4.LastUpdate=dt_string
taskf4.save()

taskf5 = TasksFamily()
taskf5.TaskFamilyName = 'Defect'
taskf5.TaskFamilyDescription = 'Link to all Defect'
taskf5.CreationDate=dt_string
taskf5.LastUpdate=dt_string
taskf5.save()

taskc1 = TasksCategory()
taskc1.TaskCategoryProjectID=1
taskc1.TaskCategoryName='Projects activity'
taskc1.TaskCategoryDescription='development part of PI Planning'
taskc1.CreationDate=dt_string
taskc1.LastUpdate=dt_string
taskc1.save()

taskc2 = TasksCategory()
taskc2.TaskCategoryProjectID=1
taskc2.TaskCategoryName='Teams activity'
taskc2.TaskCategoryDescription='development part of Sprints'
taskc2.CreationDate=dt_string
taskc2.LastUpdate=dt_string
taskc2.save()

taskc3 = TasksCategory()
taskc3.TaskCategoryProjectID=1
taskc3.TaskCategoryName='Members activity'
taskc3.TaskCategoryDescription='development part of Reports'
taskc3.CreationDate=dt_string
taskc3.LastUpdate=dt_string
taskc3.save()

taskc4 = TasksCategory()
taskc4.TaskCategoryProjectID=1
taskc4.TaskCategoryName='Admin activity'
taskc4.TaskCategoryDescription='development part of support'
taskc4.CreationDate=dt_string
taskc4.LastUpdate=dt_string
taskc4.save()

taskc5 = TasksCategory()
taskc5.TaskCategoryProjectID=1
taskc5.TaskCategoryName='General activity'
taskc5.TaskCategoryDescription='List des besoins'
taskc5.CreationDate=dt_string
taskc5.LastUpdate=dt_string
taskc5.save()

stat1=TasksStatus()
stat1.TaskStatusName='Plan'
stat1.TaskStatusDescription='To be launch'
stat1.CreationDate=dt_string
stat1.LastUpdate=dt_string

stat1.save()

stat2=TasksStatus()
stat2.TaskStatusName='In progress'
stat2.TaskStatusDescription='member working on it'
stat2.CreationDate=dt_string
stat2.LastUpdate=dt_string
stat2.save()

stat3=TasksStatus()
stat3.TaskStatusName='Not finished as plan'
stat3.TaskStatusDescription='Not delivered during Sprint'
stat3.CreationDate=dt_string
stat3.LastUpdate=dt_string
stat3.save()

stat4=TasksStatus()
stat4.TaskStatusName='Frozen'
stat4.TaskStatusDescription='Waiting information to continue'
stat4.CreationDate=dt_string
stat4.LastUpdate=dt_string
stat4.save()

stat5=TasksStatus()
stat5.TaskStatusName='Not plan'
stat5.TaskStatusDescription='Waiting Spritn decision'
stat5.CreationDate=dt_string
stat5.LastUpdate=dt_string
stat5.save()

disconnect()
