from backend_PI_mongo_model import *
from datetime import datetime


connect('PIPlanning')

now = datetime.now()
 
#print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#print("date and time =", dt_string)


project1 =Projects()
#project1.ProjectID = 1 # IDentifiant du projet
project1.ProjectName = 'PIPlanning' # Nom du projet]
project1.ProjectDescription = 'Outil de gestion de PI planning pour une équipe sélectionnée' # Description du projet
project1.ProjectPIPlanning = '22/12/2022' # Date du PI Planning
project1.ProjectPIPlanningDuration = 2 # Durée du PI Planning
project1.CreationDate = dt_string
project1.LastUpdate = dt_string
project1.save()

project2 =Projects()
#project2.ProjectID = 2 # IDentifiant du projet
project2.ProjectName = 'titi' # Nom du projet]
project2.ProjectDescription = 'test titi' # Description du projet
project2.ProjectPIPlanning = '02/02/2023' # Date du PI Planning
project2.ProjectPIPlanningDuration = 2 # Durée du PI Planning
project2.CreationDate = dt_string
project2.LastUpdate = dt_string
project2.save()


project3 =Projects()
#project3.ProjectID = 3 # IDentifiant du projet
project3.ProjectName = 'toto' # Nom du projet
project1.ProjectDescription = 'Test de plus toto'
project3.ProjectPIPlanning = '09/02/2023' # Date du PI Planning
project3.ProjectPIPlanningDuration = 2 # Durée du PI Planning
project3.CreationDate = dt_string
project3.LastUpdate = dt_string
project3.save()

team1 = Teams()
#team1.TeamID = 1
team1.TeamName = 'PI'
team1.TeamDescription = 'Developpers de la partie PI planning'
#team1.PiID = 4
team1.ProjectID = 1
team1.TeamLogo = '../imagesDB/PI.jpeg'
#team1.Archived = False
team1.CreationDate = dt_string
team1.LastUpdate = dt_string
team1.save()

team2 = Teams()
#team2.TeamID = 2
team2.TeamName = 'Sprinters'
team2.TeamDescription = 'Developpers of sprints part'
#team2.PiID = 0
team2.ProjectID = 1
team2.TeamLogo = '../imagesDB/sprinters.jpeg'
team2.Archived = False
team2.CreationDate = dt_string
team2.LastUpdate = dt_string
team2.save()

team3 = Teams()
#team3.TeamID = 3
team3.TeamName = 'tintin'
team3.TeamDescription = 'Developpers of reports part'
#team3.PiID = 4
team3.ProjectID = 1
team3TeamLogo = '../imagesDB/report.jpeg'
team3.CreationDate = dt_string
team3.LastUpdate = dt_string
team3.save()

team4 = Teams()
#team4.TeamID = 3
team4.TeamName = 'OKCorral'
team4.TeamDescription = 'Developpers of reports menu'
#team4.PiID = 5
team4.ProjectID = 2
team4.CreationDate = dt_string
team4.LastUpdate = dt_string
team4.save()

team5 = Teams()
#team5.TeamID = 6
team5.TeamName = 'SystemOnCloud'
team5.TeamDescription = 'System team of reports cloud'
#team5.PiID = 1
team5.ProjectID = 1
team5.TeamLogo = '../imagesDB/starbust.jpeg'
team5.Archived = True
team5.CreationDate = dt_string
team5.LastUpdate = dt_string
team5.save()

team6 = Teams()
#team6.TeamID = 7
team6.TeamName = 'System2023'
team6.TeamDescription = 'System team of 2023'
#team6.PiID = 0
team6.ProjectID = 2
team6TeamLogo = '../imagesDB/system.jpeg'
team6.Archived = False
team6.CreationDate = dt_string
team6.LastUpdate = dt_string
team6.save()


members1 = Members()
#members1.MemberID = 1
members1.MemberName =  'Boubert'
members1.MemberFirstName = 'Olivier'
members1.MemberEmail = 'oliboub@gmail.com'
members1.MemberAlias = 'oliboub'
members1.MemberRole = 2
members1.MemberTheme = 'LightBlue2'
members1.MemberAdmin = False
members1.MemberFirstConnection = True
members1.CreationDate = dt_string
members1.LastUpdate = dt_string
members1.save()

members2 = Members()
#members2.MemberID = 2
members2.MemberName =  'TVV'
members2.MemberFirstName = 'MC'
members2.MemberEmail = 'mctvv@toto.com'
members2.MemberAlias = 'MacFly'
members2.MemberRole = 4
members2.MemberTheme = 'LightBlue2'
members2.MemberFirstConnection = True
members2.CreationDate = dt_string
members2.LastUpdate = dt_string
members2.save()

members3 = Members()
#members3.MemberID = 3
members3.MemberName =  'Tartuffe'
members3.MemberFirstName = 'Claudio'
members3.MemberEmail = 'ctartuffe@gmail.com'
members3.MemberAlias = 'CrackCl'
members3.MemberRole = 1
members3.MemberTheme = 'LightBlue2'
members3.CreationDate = dt_string
members3.LastUpdate = dt_string
members3.save()

members4 = Members()
#members4.MemberID = 4
members4.MemberName =  'scrumol'
members4.MemberFirstName = 'sprinter'
members4.MemberEmail = 'scrumolse@gmail.com'
members4.MemberAlias = 'scrumol'
members4.MemberRole = 3
members4.MemberTheme = 'LightBlue2'
members4.CreationDate = dt_string
members4.LastUpdate = dt_string
members4.save()

members5 = Members()
#members1.MemberID = 1
members5.MemberName =  'admin'
members5.MemberFirstName = 'admin'
members5.MemberEmail = 'admin@gmail.com'
members5.MemberAlias = 'admintop'
members5.MemberRole = 5
members5.MemberTheme = 'LightBlue2'
members5.MemberAdmin = True
members5.CreationDate = dt_string
members5.LastUpdate = dt_string
members5.save()

PiTeams1 = Piteams()
PiTeams1.PiID = 4
PiTeams1.TeamID = 1
PiTeams1.save()

PiTeams2 = Piteams()
PiTeams2.PiID = 4
PiTeams2.TeamID = 2
PiTeams2.save()


PiTeams3 = Piteams()
PiTeams3.PiID = 4
PiTeams3.TeamID = 3
PiTeams3.save()

PiTeams4 = Piteams()
PiTeams4.PiID = 1
PiTeams4.TeamID = 4
PiTeams4.save()

PiTeams5 = Piteams()
PiTeams5.PiID = 3
PiTeams5.TeamID = 5
PiTeams5.save()

role1= Roles()
#role1.RoleID=1
role1.RoleName ="Developper"
role1.RoleDescription ="Developper de solution"
role1.CreationDate = dt_string
role1.LastUpdate = dt_string
role1.save()

role2= Roles()
#role2.RoleID=2
role2.RoleName ="Solution Owner"
role2.RoleDescription ="Responsable de libraison d'une équipe agile et de livrer les objectifs du PI"
role2.CreationDate = dt_string
role2.LastUpdate = dt_string
role2.save()

role3= Roles()
#role3.RoleID=3
role3.RoleName ="Product Owner"
role3.RoleDescription ="Responsable client des objectifs d'un PI"
role3.CreationDate = dt_string
role3.LastUpdate = dt_string
role3.save()

role4= Roles()
#role4.RoleID=4
role4.RoleName ="Scrum Master"
role4.RoleDescription ="Animateur d'équipe"
role4.CreationDate = dt_string
role4.LastUpdate = dt_string
role4.save()

role5= Roles()
#role5.RoleID=5
role5.RoleName ="admin"
role5.RoleDescription ="administrateur de l'outil)"
role5.CreationDate = dt_string
role5.LastUpdate = dt_string
role5.save()

#-------------

alloc1 =LinkMemberTeam()
#alloc1.AllocationID = 1
alloc1.MemberID = 1
alloc1.TeamID = 1
alloc1.save()

alloc2 =LinkMemberTeam()
#alloc2.AllocationID = 2
alloc2.MemberID = 2
alloc2.TeamID = 1
alloc2.save()

alloc3 =LinkMemberTeam()
#alloc2.AllocationID = 2
alloc3.MemberID = 3
alloc3.TeamID = 2
alloc3.save()

alloc4 =LinkMemberTeam()
#alloc2.AllocationID = 2
alloc4.MemberID = 4
alloc4.TeamID = 2
alloc4.save()

alloc5 =LinkMemberTeam()
#alloc2.AllocationID = 2
alloc5.MemberID = 5
alloc5.TeamID = 1
alloc5.save()

sprint1=Sprints()
#sprint1.SprintID = 1
sprint1.PiID = 1
sprint1.SprintSeq = 1
sprint1.SprintDays = 20
sprint1.SprintStartDate = '06/02/2023'
sprint1.CreationDate = dt_string
sprint1.LastUpdate = dt_string
sprint1.save()

sprint2=Sprints()
#sprint2.SprintID = 2
sprint2.PiID = 1
sprint2.SprintSeq = 2
sprint2.SprintDays = 20
sprint2.SprintStartDate = '20/02/2023'
sprint2.CreationDate = dt_string
sprint2.LastUpdate = dt_string
sprint2.save()

sprint3=Sprints()
#sprint2.SprintID = 2
sprint3.PiID = 6
sprint3.SprintSeq = 2
sprint3.SprintDays = 20
sprint3.SprintStartDate = '20/02/2023'
sprint3.CreationDate = dt_string
sprint3.LastUpdate = dt_string
sprint3.save()


pi11= PiPlan()
#pi11.PiID = 1
pi11.ProjectID = 1
pi11.PiCurrent = True
pi11.PiNumber = 1
pi11.PiTeams = 2
pi11.PiSprintWeeks = 2
pi11.PiSprintQtt = 4
pi11.PiArchived = False
pi11.CreationDate = dt_string
pi11.LastUpdate = dt_string
pi11.save()

pi12 = PiPlan()
#pi12.PiID = 2
pi12.ProjectID = 1
pi12.PiNumber = 2
pi12.PiTeams = 2
pi12.PiSprintWeeks = 2
pi12.PiSprintQtt = 4
pi12.PiArchived = False
pi12.CreationDate = dt_string
pi12.LastUpdate = dt_string
pi12.save()

pi13 = PiPlan()
#pi13.PiID = 3
pi13.ProjectID = 1
pi13.PiNumber = 3
pi13.PiTeams = 2
pi13.PiSprintWeeks = 2
pi13.PiSprintQtt = 4
pi13.PiArchived = False
pi13.CreationDate = dt_string
pi13.LastUpdate = dt_string
pi13.save()

pi14= PiPlan()
#pi14.PiID = 4
pi14.ProjectID = 1
pi14.PiNumber = 4
pi14.PiTeams = 2
pi14.PiSprintWeeks = 2
pi14.PiSprintQtt = 4
pi14.PiArchived = False
pi14.CreationDate = dt_string
pi14.LastUpdate = dt_string
pi14.save()

pi15= PiPlan()
#pi15.PiID = 7
pi15.ProjectID = 1
pi15.PiNumber = 5
pi15.PiTeams = 2
pi15.PiSprintWeeks = 2
pi15.PiSprintQtt = 4
pi15.PiArchived = False
pi15.CreationDate = dt_string
pi15.LastUpdate = dt_string
pi15.save()

pi21= PiPlan()
#pi21.PiID = 5
pi21.ProjectID = 2
pi21.PiNumber = 1
pi21.PiTeams = 1
pi21.PiSprintWeeks = 2
pi21.PiSprintQtt = 4
pi21.PiArchived = False
pi21.CreationDate = dt_string
pi21.LastUpdate = dt_string
pi21.save()

pi22= PiPlan()
#pi22.PiID = 6
pi22.ProjectID = 2
pi22.PiNumber = 2
pi22.PiTeams = 1
pi22.PiSprintWeeks = 2
pi22.PiSprintQtt = 4
pi22.PiArchived = False
pi22.CreationDate = dt_string
pi22.LastUpdate = dt_string
pi22.save()

capa1 = Capacity()
#capa1.CapacityID = 1
capa1.SprintID = 1
capa1.MemberID = 1
capa1.CapacityDays = 40
capa1.MissingDays = 0
capa1.save()

capa2 = Capacity()
#capa2.CapacityID = 2
capa2.SprintID = 2
capa2.MemberID = 1
capa2.CapacityDays = 30
capa2.MissingDays = 10
capa2.save()

linkmr1 = LinkMemberRole()
linkmr1.MemberID = 1
linkmr1.RoleID = 2
linkmr1.save()

linkmr2 = LinkMemberRole()
linkmr2.MemberID = 2
linkmr2.RoleID = 1
linkmr2.save()

linkmr3 = LinkMemberRole()
linkmr3.MemberID = 3
linkmr3.RoleID = 1
linkmr3.save()

linkmr4 = LinkMemberRole()
linkmr4.MemberID = 4
linkmr4.RoleID = 3
linkmr4.save()

linkmr5 = LinkMemberRole()
linkmr5.MemberID = 5
linkmr5.RoleID = 5
linkmr5.save()


disconnect()
