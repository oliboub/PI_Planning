#import bcrypt
from mongoengine import *
from backend_PI_mongo_model import *
from datetime import datetime


### Teams
def create_team(projectID, team, description, logo):
    print('fonction: create_team(',projectID,',',team,',',description,',',logo,')')
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    team1=Teams()
    team1.ProjectID = projectID
    team1.TeamName = team
    team1.TeamDescription = description
    team1.TeamLogo = logo
    team1.CreationDate = creationdate
    team1.LastUpdate = creationdate
    team1.save()

def list_teams_all(projectid=None):
    print('fonction: list_teams_all')
    team = Teams.objects(TeamArchived=False,ProjectID=projectid)
    print('Team\t\t - \t Project')
    team1= []
    list_teams=[]
    for team1 in team:
        print(team1.TeamID,team1.ProjectID)
        projectname = Projects.objects(ProjectID=team1.ProjectID).first()
        if projectname is None:
            projectname='Non allocated'
        print(projectname.ProjectName)
        teams=[projectname.ProjectName,team1.TeamName,team1.TeamDescription,team1.TeamLogo]
        list_teams.append(teams)
#    print(list_teams)
#    print(list_teams[0][1])
    return(list_teams)


def list_teams_by_project(pname):
    print('fonction: list_teams_all')
    list_teams=[]
    project=Projects.objects(ProjectName=pname).first()
    pid=project.ProjectID
    team = Teams.objects(Archived=False,ProjectID=pid)
#    print("Project:",pname)
#    print('Teams')
 
    for team1 in team:
#        print(pname,team1.TeamName,team1.TeamID,team1.ProjectID,team1.TeamDescription,team1.TeamLogo)
        teams=[pname,team1.TeamName,team1.TeamDescription,team1.TeamLogo]
        list_teams.append(teams)
#    print(list_teams)
    return(list_teams)

print(__name__,'imported')


### renvoie la liste des equipes par page et en fonciton du project ID
def list_teams_page(page,projectid=None):
    print(__name__,'projectid',projectid)
    if projectid == None:
        teams = Teams.objects(Archived=False).paginate(page,5)
    else:
        teams = Teams.objects(ProjectID=projectid,Archived=False).paginate(page,5)
           
#    for a in teams.items:
#        print(a.TeamName,'\t',a.TeamDescription,'\t',a.TeamLogo,'\t',a.ProjectID)
    return teams