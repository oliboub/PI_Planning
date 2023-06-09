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
task1.CreatedByID = 5
task1.CreationDate=dt_string
task1.UpdatedByID=5
task1.LastUpdate=dt_string
task1.save()

taskl1 = TasksDescriptionLink()
taskl1.TaskID=1
taskl1.TaskDescriptionID=1
taskl1.CreatedByID = 5
taskl1.CreationDate=dt_string
taskl1.UpdatedByID=5
taskl1.LastUpdate=dt_string
taskl1.save()

taskl2 = TasksDescriptionLink()
taskl2.TaskID=1
taskl2.TaskDescriptionID=2
taskl2.CreatedByID = 5
taskl2.CreationDate=dt_string
taskl2.UpdatedByID=5
taskl2.LastUpdate=dt_string
taskl2.save()

taskl3 = TasksDescriptionLink()
taskl3.TaskID=2
taskl3.TaskDescriptionID=3
taskl3.CreatedByID = 5
taskl3.CreationDate=dt_string
taskl3.UpdatedByID=5
taskl3.LastUpdate=dt_string
taskl3.save()


taskd1 = TasksDescription()
taskd1.TaskDescription="use case: en cas d'audit et de besoin d'analyse, nous devons etre capable de donner toutes les logs d'acivités à un data scientist"
taskd1.CreatedByID = 5
taskd1.CreationDate = dt_string
taskd1.UpdatedByID=5
taskd1.LastUpdate = dt_string
taskd1.save()

taskd2 = TasksDescription()
taskd2.TaskDescription="On essaye de penser data science as concept"
taskd2.CreatedByID = 5
taskd2.CreationDate=dt_string
taskd2.UpdatedByID=5
taskd2.LastUpdate=dt_string
taskd2.save()

taskd3 = TasksDescription()
taskd3.TaskDescription="Encore un peu de detail pour prendre la décision qui s'impose. On a pas tous les jours 20 ans et ça fait mal."
taskd2.CreatedByID = 5
taskd3.CreationDate=dt_string
taskd3.UpdatedByID=5
taskd3.LastUpdate=dt_string
taskd3.save()


taskf1 = TasksFamily()
taskf1.TaskFamilyName = 'Epic'
taskf1.TaskFamilyDescription = 'Link to all Epic'
taskf1.CreatedByID = 5
taskf1.CreationDate=dt_string
taskf1.UpdatedByID=5
taskf1.LastUpdate=dt_string
taskf1.save()

taskf2 = TasksFamily()
taskf2.TaskFamilyName = 'Capability'
taskf2.TaskFamilyDescription = 'Link to all Capabiliy'
taskf2.CreatedByID = 5
taskf2.CreationDate=dt_string
taskf2.UpdatedByID=5
taskf2.LastUpdate=dt_string
taskf2.save()

taskf3 = TasksFamily()
taskf3.TaskFamilyName = 'Feature'
taskf3.TaskFamilyDescription = 'Link to all features'
taskf3.CreatedByID = 5
taskf3.CreationDate=dt_string
taskf3.LastUpdate=dt_string
taskf3.save()

taskf4 = TasksFamily()
taskf4.TaskFamilyName = 'Story'
taskf4.TaskFamilyDescription = 'Link to all Story'
taskf4.CreatedByID = 5
taskf4.CreationDate=dt_string
taskf4.UpdatedByID=5
taskf4.LastUpdate=dt_string
taskf4.save()

taskf5 = TasksFamily()
taskf5.TaskFamilyName = 'Defect'
taskf5.TaskFamilyDescription = 'Link to all Defect'
taskf5.CreatedByID = 5
taskf5.CreationDate=dt_string
taskf5.UpdatedByID=5
taskf5.LastUpdate=dt_string
taskf5.save()

taskf6 = TasksFamily()
taskf6.TaskFamilyName = 'Objective'
taskf6.TaskFamilyDescription = 'Link to all Objective'
taskf6.CreatedByID = 5
taskf6.CreationDate=dt_string
taskf6.UpdatedByID=5
taskf6.LastUpdate=dt_string
taskf5.save()


taskc0 = TasksCategory()
taskc0.TaskCategoryProjectID=1
taskc0.TaskCategoryName='To be defined'
taskc0.TaskCategoryDescription='Taks category to be defined'
taskc0.CreatedByID = 5
taskc0.CreationDate=dt_string
taskc0.UpdatedByID=5
taskc0.LastUpdate=dt_string
taskc0.save()

taskc1 = TasksCategory()
taskc1.TaskCategoryProjectID=1
taskc1.TaskCategoryName='Projects activity'
taskc1.TaskCategoryDescription='development part of PI Planning'
taskc1.CreatedByID = 5
taskc1.CreationDate=dt_string
taskc1.UpdatedByID=5
taskc1.LastUpdate=dt_string
taskc1.save()

taskc2 = TasksCategory()
taskc2.TaskCategoryProjectID=1
taskc2.TaskCategoryName='Teams activity'
taskc2.TaskCategoryDescription='development part of Sprints'
taskc2.CreatedByID = 5
taskc2.CreationDate=dt_string
taskc2.UpdatedByID=5
taskc2.LastUpdate=dt_string
taskc2.save()

taskc3 = TasksCategory()
taskc3.TaskCategoryProjectID=1
taskc3.TaskCategoryName='Members activity'
taskc3.TaskCategoryDescription='development part of Reports'
taskc3.CreatedByID = 5
taskc3.CreationDate=dt_string
taskc3.UpdatedByID=5
taskc3.LastUpdate=dt_string
taskc3.save()

taskc4 = TasksCategory()
taskc4.TaskCategoryProjectID=1
taskc4.TaskCategoryName='Admin activity'
taskc4.TaskCategoryDescription='development part of support'
taskc4.CreatedByID = 5
taskc4.CreationDate=dt_string
taskc4.UpdatedByID=5
taskc4.LastUpdate=dt_string
taskc4.save()

taskc5 = TasksCategory()
taskc5.TaskCategoryProjectID=1
taskc5.TaskCategoryName='Portfolio activity'
taskc5.TaskCategoryDescription='Actions necesary for portfolio management'
taskc5.CreatedByID = 5
taskc5.CreationDate=dt_string
taskc5.UpdatedByID=5
taskc5.LastUpdate=dt_string
taskc5.save()

stat0=TasksStatus()
stat0.TaskStatusName='Backlog'
stat0.TaskStatusDescription='Backlog, waiting PI Planning decision'
stat0.CreatedByID = 5
stat0.CreationDate=dt_string
stat0.UpdatedByID=5
stat0.LastUpdate=dt_string
stat0.save()

stat1=TasksStatus()
stat1.TaskStatusName='Plan'
stat1.TaskStatusDescription='To be launch'
stat1.CreatedByID = 5
stat1.CreationDate=dt_string
stat1.UpdatedByID=5
stat1.LastUpdate=dt_string
stat1.save()

stat2=TasksStatus()
stat2.TaskStatusName='In progress'
stat2.TaskStatusDescription='member working on it'
stat2.CreatedByID = 5
stat2.CreationDate=dt_string
stat2.UpdatedByID=5
stat2.LastUpdate=dt_string
stat2.save()

stat3=TasksStatus()
stat3.TaskStatusName='Not finished as plan'
stat3.TaskStatusDescription='Not delivered during Sprint'
stat3.CreatedByID = 5
stat3.CreationDate=dt_string
stat3.UpdatedByID=5
stat3.LastUpdate=dt_string
stat3.save()

stat4=TasksStatus()
stat4.TaskStatusName='Frozen'
stat4.TaskStatusDescription='Waiting information to continue'
stat4.CreatedByID = 5
stat4.CreationDate=dt_string
stat4.UpdatedByID=5
stat4.LastUpdate=dt_string
stat4.save()

stat5=TasksStatus()
stat5.TaskStatusName='Not plan'
stat5.TaskStatusDescription='Waiting Sprint decision'
stat5.CreatedByID = 5
stat5.CreationDate=dt_string
stat5.UpdatedByID=5
stat5.LastUpdate=dt_string
stat5.save()

dep1=TasksDependencyCategory()
dep1.TaskDependencyCategoryName='Parent'
dep1.TaskDependencyCategoryDescription='The task source is parent of task target'
dep1.CreatedByID = 5
dep1.CreationDate=dt_string
dep1.UpdatedByID=5
dep1.LastUpdate=dt_string
dep1.save()

dep2=TasksDependencyCategory()
dep2.TaskDependencyCategoryName='Child'
dep2.TaskDependencyCategoryDescription='The task target is parent of task source'
dep2.CreatedByID = 5
dep2.CreationDate=dt_string
dep2.UpdatedByID=5
dep2.LastUpdate=dt_string
dep2.save()

dep3=TasksDependencyCategory()
dep3.TaskDependencyCategoryName='Link'
dep3.TaskDependencyCategoryDescription='The task target is linked to task source'
dep3.CreatedByID = 5
dep3.CreationDate=dt_string
dep3.UpdatedByID=5
dep3.LastUpdate=dt_string
dep3.save()

disconnect()
