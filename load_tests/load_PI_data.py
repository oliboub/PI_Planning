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
project1.CreatedByID=5
project1.CreationDate = dt_string
project1.UpdatedByID=5
project1.LastUpdate = dt_string
project1.save()

project2 =Projects()
#project2.ProjectID = 2 # IDentifiant du projet
project2.ProjectName = 'Titi' # Nom du projet]
project2.ProjectDescription = 'Test titi' # Description du projet
project2.ProjectPIPlanning = '02/02/2023' # Date du PI Planning
project2.ProjectPIPlanningDuration = 2 # Durée du PI Planning
project2.CreatedByID=5
project2.CreationDate = dt_string
project2.UpdatedByID=5
project2.LastUpdate = dt_string
project2.save()


project3 =Projects()
project3.ProjectName = 'Toto' # Nom du projet
project3.ProjectDescription = 'Essai en vol'
project3.ProjectPIPlanning = '09/02/2023' # Date du PI Planning
project3.ProjectPIPlanningDuration = 2 # Durée du PI Planning
project3.CreatedByID=5
project3.CreationDate = dt_string
project3.UpdatedByID=5
project3.LastUpdate = dt_string
project3.save()

project4 =Projects()
project4.ProjectName = 'Tata' # Nom du projet
project4.ProjectDescription = 'Taratata music box'
project4.ProjectPIPlanning = '09/02/2023' # Date du PI Planning
project4.ProjectPIPlanningDuration = 2 # Durée du PI Planning
project4.CreatedByID=5
project4.CreationDate = dt_string
project4.UpdatedByID=5
project4.LastUpdate = dt_string
project4.save()

project5 =Projects()
project5.ProjectName = 'Tutu' # Nom du projet
project5.ProjectDescription = 'Turlututu chapeau pointu'
project5.ProjectPIPlanning = '09/02/2023' # Date du PI Planning
project5.ProjectPIPlanningDuration = 2 # Durée du PI Planning
project5.CreatedByID=5
project5.CreationDate = dt_string
project5.UpdatedByID=5
project5.LastUpdate = dt_string
project5.save()


team1 = Teams()
team1.TeamName = 'PI'
team1.TeamDescription = 'Developpers de la partie PI planning'
team1.ProjectID = 1
team1.TeamLogo = '../imagesDB/PI.jpeg'
team1.CreatedByID=5
team1.CreationDate = dt_string
team1.UpdatedByID=5
team1.LastUpdate = dt_string
team1.save()

team2 = Teams()
team2.TeamName = 'Sprinters'
team2.TeamDescription = 'Developpers of sprints part'
team2.ProjectID = 1
team2.TeamLogo = '../imagesDB/sprinters.jpeg'
team2.CreatedByID=5
team2.CreationDate = dt_string
team2.UpdatedByID=5
team2.LastUpdate = dt_string
team2.Archived = False
team2.save()

team3 = Teams()
team3.TeamName = 'Tintin'
team3.TeamDescription = 'Developpers of reports part'
team3.ProjectID = 1
team3.TeamLogo = '../imagesDB/report.jpeg'
team3.CreatedByID=5
team3.CreationDate = dt_string
team3.UpdatedByID=5
team3.LastUpdate = dt_string
team3.save()

team4 = Teams()
team4.TeamName = 'OKCorral'
team4.TeamDescription = 'Developpers of reports menu'
team4.TeamLogo = '../imagesDB/ok-corral-sign.jpg'
team4.ProjectID = 2
team4.CreatedByID=5
team4.CreationDate = dt_string
team4.UpdatedByID=5
team4.LastUpdate = dt_string
team4.save()

team5 = Teams()
team5.TeamName = 'SystemOnCloud'
team5.TeamDescription = 'System team of reports cloud'
team5.ProjectID = 1
team5.TeamLogo = '../imagesDB/cloud.jpg'
team5.CreatedByID=5
team5.CreationDate = dt_string
team5.UpdatedByID=5
team5.LastUpdate = dt_string
team5.Archived = True
team5.save()

team6 = Teams()
team6.TeamName = 'System2023'
team6.TeamDescription = 'System team of 2023'
team6.ProjectID = 2
team6.TeamLogo = '../imagesDB/system.jpeg'
team6.CreatedByID=5
team6.CreationDate = dt_string
team6.UpdatedByID=5
team6.LastUpdate = dt_string
team6.Archived = False
team6.save()

team7 = Teams()
team7.TeamName = 'Applepie'
team7.TeamDescription = 'Team to define size of pies'
team7.ProjectID = 1
team7.TeamLogo = '../imagesDB/applepie.jpg'
team7.CreatedByID=5
team7.CreationDate = dt_string
team7.LastUpdate = dt_string
team7.Archived = False
team7.save()

team8 = Teams()
team8.TeamName = 'Taskers'
team8.TeamDescription = 'Team to work on tasks'
team8.ProjectID = 2
team8.TeamLogo = '../imagesDB/starburst.jpeg'
team8.CreatedByID=5
team8.CreationDate = dt_string
team8.UpdatedByID=5
team8.LastUpdate = dt_string
team8.Archived = False
team8.save()

team9 = Teams()
team9.TeamName = 'Deep learning'
team9.TeamDescription = 'Analyze how to reuse our data to progress'
team9.ProjectID = 4
team9.TeamLogo = '../imagesDB/reseau_neuronal.jpg'
team9.CreatedByID=5
team9.CreationDate = dt_string
team9.UpdatedByID=5
team9.LastUpdate = dt_string
team9.Archived = False
team9.save()

#-----

members1 = Members()
#members1.MemberID = 1
members1.MemberName =  'Boubert'
members1.MemberFirstName = 'Olivier'
members1.MemberEmail = 'oliboubr@toto.com'
members1.MemberAlias = 'oliboub'
members1.MemberRole = 2
members1.MemberTheme = 'LightBlue2'
members1.MemberAdmin = False
members1.MemberFirstConnection = True
members1.CreatedByID = 5
members1.CreationDate = dt_string
members1.UpdatedByID=5
members1.LastUpdate = dt_string
members1.save()

members2 = Members()
#members2.MemberID = 2
members2.MemberName =  'Tuitui'
members2.MemberFirstName = 'MC'
members2.MemberEmail = 'tuitui@toto.com'
members2.MemberAlias = 'MacFly'
members2.MemberRole = 4
members2.MemberTheme = 'LightBlue2'
members2.MemberFirstConnection = True
members2.CreatedByID = 5
members2.CreationDate = dt_string
members2.UpdatedByID=5
members2.LastUpdate = dt_string
members2.save()

members3 = Members()
#members3.MemberID = 3
members3.MemberName =  'Tartuffe'
members3.MemberFirstName = 'Claudio'
members3.MemberEmail = 'ctartuffe@toto.com'
members3.MemberAlias = 'CrackCl'
members3.MemberRole = 1
members3.MemberTheme = 'LightBlue2'
members3.CreatedByID = 5
members3.CreationDate = dt_string
members3.UpdatedByID=5
members3.LastUpdate = dt_string
members3.save()

members4 = Members()
#members4.MemberID = 4
members4.MemberName =  'Scrumol'
members4.MemberFirstName = 'Sprinter'
members4.MemberEmail = 'scrumolse@toto.com'
members4.MemberAlias = 'scrumol'
members4.MemberRole = 3
members4.MemberTheme = 'LightBlue2'
members4.CreatedByID = 5
members4.CreationDate = dt_string
members4.UpdatedByID=5
members4.LastUpdate = dt_string
members4.save()

members5 = Members()
members5.MemberName =  'Admin'
members5.MemberFirstName = 'Admin'
members5.MemberEmail = 'admin@toto.com'
members5.MemberAlias = 'admintop'
members5.MemberRole = 5
members5.MemberTheme = 'LightBlue2'
members5.MemberAdmin = True
members5.CreatedByID = 5
members5.CreationDate = dt_string
members5.UpdatedByID=5
members5.LastUpdate = dt_string
members5.save()

members6 = Members()
members6.MemberName =  'Retail'
members6.MemberFirstName = 'Valentin'
members6.MemberEmail = 'rte@toto.com'
members6.MemberAlias = 'rtelead'
members6.MemberRole = 7
members6.MemberTheme = 'LightBlue2'
members6.MemberPortfolio = True
members6.CreatedByID = 5
members6.CreationDate = dt_string
members6.UpdatedByID=5
members6.LastUpdate = dt_string
members6.save()

members7 = Members()
members7.MemberName =  'Aladin'
members7.MemberFirstName = 'Magic'
members7.MemberEmail = 'magical@toto.com'
members7.MemberAlias = 'magical'
members7.MemberRole = 3
members7.MemberTheme = 'LightBlue2'
members7.MemberPortfolio = False
members7.CreatedByID = 5
members7.CreationDate = dt_string
members7.UpdatedByID=5
members7.LastUpdate = dt_string
members7.save()

members8 = Members()
members8.MemberName =  'Arthur'
members8.MemberFirstName = 'Roi'
members8.MemberEmail = 'kingart@toto.com'
members8.MemberAlias = 'kingart'
members8.MemberRole = 2
members8.MemberTheme = 'LightBlue2'
members8.MemberPortfolio = False
members8.CreatedByID = 5
members8.CreationDate = dt_string
members8.UpdatedByID=5
members8.LastUpdate = dt_string
members8.save()

members9 = Members()
members9.MemberName =  'Facile'
members9.MemberFirstName = 'Itateur'
members9.MemberEmail = 'facilitateur@toto.com'
members9.MemberAlias = 'facilitateur'
members9.MemberRole = 4
members9.MemberTheme = 'LightBlue2'
members9.MemberPortfolio = False
members9.CreatedByID = 5
members9.CreationDate = dt_string
members9.UpdatedByID=5
members9.LastUpdate = dt_string
members9.save()

members10 = Members()
members10.MemberName =  'Parson'
members10.MemberFirstName = 'Alain'
members10.MemberEmail = 'synthezic@toto.com'
members10.MemberAlias = 'synthezic'
members10.MemberRole = 1
members10.MemberTheme = 'LightBlue2'
members10.MemberPortfolio = False
members10.CreatedByID = 5
members10.CreationDate = dt_string
members10.UpdatedByID=5
members10.LastUpdate = dt_string
members10.save()

members11 = Members()
members11.MemberName =  'Buzzee'
members11.MemberFirstName = 'Berndt'
members11.MemberEmail = 'buz1@toto.com'
members11.MemberAlias = 'Buziness1'
members11.MemberRole = 6
members11.MemberTheme = 'LightBlue2'
members11.MemberPortfolio = False
members11.CreatedByID = 5
members11.CreationDate = dt_string
members11.UpdatedByID=5
members11.LastUpdate = dt_string
members11.save()


PiTeams1 = Piteams()
PiTeams1.PiID = 4
PiTeams1.TeamID = 1
PiTeams1.CreatedByID = 5
PiTeams1.CreationDate = dt_string
PiTeams1.LastUpdate = dt_string
PiTeams1.save()

PiTeams2 = Piteams()
PiTeams2.PiID = 4
PiTeams2.TeamID = 2
PiTeams2.CreatedByID = 5
PiTeams2.CreationDate = dt_string
PiTeams2.LastUpdate = dt_string
PiTeams2.save()


PiTeams3 = Piteams()
PiTeams3.PiID = 4
PiTeams3.TeamID = 3
PiTeams3.CreatedByID = 5
PiTeams3.CreationDate = dt_string
PiTeams3.LastUpdate = dt_string
PiTeams3.save()

PiTeams4 = Piteams()
PiTeams4.PiID = 1
PiTeams4.TeamID = 4
PiTeams4.CreatedByID = 5
PiTeams4.CreationDate = dt_string
PiTeams4.LastUpdate = dt_string
PiTeams4.save()

PiTeams5 = Piteams()
PiTeams5.PiID = 3
PiTeams5.TeamID = 5
PiTeams5.CreatedByID = 5
PiTeams5.CreationDate = dt_string
PiTeams5.LastUpdate = dt_string
PiTeams5.save()

role1= Roles()
#role1.RoleID=1
role1.RoleName ="Developper"
role1.RoleDescription ="Developper de solution"
role1.CreatedByID = 5
role1.CreationDate = dt_string
role1.LastUpdate = dt_string
role1.save()

role2= Roles()
#role2.RoleID=2
role2.RoleName ="Solution Owner"
role2.RoleDescription ="Responsable de livraison d'une équipe agile et de livrer les objectifs du PI"
role2.CreatedByID = 5
role2.CreationDate = dt_string
role2.LastUpdate = dt_string
role2.save()

role3= Roles()
#role3.RoleID=3
role3.RoleName ="Product Owner"
role3.RoleDescription ="Responsable client des objectifs d'un PI"
role3.CreatedByID = 5
role3.CreationDate = dt_string
role3.LastUpdate = dt_string
role3.save()

role4= Roles()
#role4.RoleID=4
role4.RoleName ="Scrum Master"
role4.RoleDescription ="Animateur d'équipe"
role4.CreatedByID = 5
role4.CreationDate = dt_string
role4.LastUpdate = dt_string
role4.save()

role5= Roles()
#role5.RoleID=5
role5.RoleName ="admin"
role5.RoleDescription ="administrateur de l'outil"
role5.CreatedByID = 5
role5.CreationDate = dt_string
role5.LastUpdate = dt_string
role5.save()

role6= Roles()
role6.RoleName ="Business Owner"
role6.RoleDescription ="Business Owner"
role6.CreatedByID = 5
role6.CreationDate = dt_string
role6.LastUpdate = dt_string
role6.save()

role7= Roles()
role7.RoleName ="Portfolio"
role7.RoleDescription ="Portfolio manager"
role7.CreatedByID = 5
role7.CreationDate = dt_string
role7.LastUpdate = dt_string
role7.save()


#-------------

alloc1 =LinkMemberTeam()
#alloc1.AllocationID = 1
alloc1.MemberID = 1
alloc1.TeamID = 1
alloc1.CreatedByID = 5
alloc1.CreationDate=dt_string
alloc1.LastUpdate=dt_string
alloc1.save()

alloc2 =LinkMemberTeam()
#alloc2.AllocationID = 2
alloc2.MemberID = 2
alloc2.TeamID = 1
alloc2.CreatedByID = 5
alloc2.CreationDate=dt_string
alloc2.LastUpdate=dt_string
alloc2.save()

alloc3 =LinkMemberTeam()
alloc3.MemberID = 3
alloc3.TeamID = 2
alloc3.CreatedByID = 5
alloc3.CreationDate=dt_string
alloc3.LastUpdate=dt_string
alloc3.save()

alloc4 =LinkMemberTeam()
alloc4.MemberID = 4
alloc4.TeamID = 2
alloc4.CreatedByID = 5
alloc4.CreationDate=dt_string
alloc4.LastUpdate=dt_string
alloc4.save()

alloc5 =LinkMemberTeam()
alloc5.MemberID = 5
alloc5.TeamID = 1
alloc5.CreatedByID = 5
alloc5.CreationDate=dt_string
alloc5.LastUpdate=dt_string
alloc5.save()

alloc6 =LinkMemberTeam()
alloc6.MemberID = 6
alloc6.TeamID = 1
alloc6.CreatedByID = 5
alloc6.CreationDate=dt_string
alloc6.LastUpdate=dt_string
alloc6.save()

alloc7 =LinkMemberTeam()
#alloc2.AllocationID = 2
alloc7.MemberID = 7
alloc7.TeamID = 3
alloc7.save()

alloc8 =LinkMemberTeam()
alloc8.MemberID = 8
alloc8.TeamID = 2
alloc8.CreatedByID = 5
alloc8.CreationDate=dt_string
alloc8.LastUpdate=dt_string
alloc8.save()

alloc9=LinkMemberTeam()
alloc9.MemberID = 9
alloc9.TeamID = 2
alloc9.CreatedByID = 5
alloc9.CreationDate=dt_string
alloc9.LastUpdate=dt_string
alloc9.save()

alloc10=LinkMemberTeam()
alloc10.MemberID = 10
alloc10.TeamID = 4
alloc10.CreatedByID = 5
alloc10.CreationDate=dt_string
alloc10.LastUpdate=dt_string
alloc10.save()

alloc11=LinkMemberTeam()
alloc11.MemberID = 11
alloc11.TeamID = 4
alloc11.CreatedByID = 5
alloc11.CreationDate=dt_string
alloc11.LastUpdate=dt_string
alloc11.save()

sprint1=Sprints()
sprint1.PiID = 1
sprint1.SprintSeq = 1
sprint1.SprintDays = 20
sprint1.SprintStartDate = '06/02/2023'
sprint1.CreatedByID = 5
sprint1.CreationDate = dt_string
sprint1.LastUpdate = dt_string
sprint1.save()

sprint2=Sprints()
sprint2.PiID = 1
sprint2.SprintSeq = 2
sprint2.SprintDays = 20
sprint2.SprintStartDate = '20/02/2023'
sprint2.CreatedByID = 5
sprint2.CreationDate = dt_string
sprint2.LastUpdate = dt_string
sprint2.save()

sprint3=Sprints()
sprint3.PiID = 6
sprint3.SprintSeq = 2
sprint3.SprintDays = 20
sprint3.CreatedByID = 5
sprint3.SprintStartDate = '20/02/2023'
sprint3.CreationDate = dt_string
sprint3.LastUpdate = dt_string
sprint3.save()

pi11= PiPlan()
pi11.ProjectID = 1
pi11.PiCurrent = True
pi11.PiNumber = 1
pi11.PiTeams = 2
pi11.PiSprintWeeks = 2
pi11.PiSprintQtt = 4
pi11.PiArchived = False
pi11.CreatedByID = 5
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
pi12.CreatedByID = 5
pi12.CreationDate = dt_string
pi12.LastUpdate = dt_string
pi12.save()

pi13 = PiPlan()
pi13.ProjectID = 1
pi13.PiNumber = 3
pi13.PiTeams = 2
pi13.PiSprintWeeks = 2
pi13.PiSprintQtt = 4
pi13.PiArchived = False
pi13.CreatedByID = 5
pi13.CreationDate = dt_string
pi13.LastUpdate = dt_string
pi13.save()

pi14= PiPlan()
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
pi15.ProjectID = 1
pi15.PiNumber = 5
pi15.PiTeams = 2
pi15.PiSprintWeeks = 2
pi15.PiSprintQtt = 4
pi15.PiArchived = False
pi15.CreatedByID = 5
pi15.CreationDate = dt_string
pi15.LastUpdate = dt_string
pi15.save()

pi21= PiPlan()
pi21.ProjectID = 2
pi21.PiNumber = 1
pi21.PiTeams = 1
pi21.PiSprintWeeks = 2
pi21.PiSprintQtt = 4
pi21.PiArchived = False
pi21.CreatedByID = 5
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
pi22.CreatedByID = 5
pi22.CreationDate = dt_string
pi22.LastUpdate = dt_string
pi22.save()

capa1 = Capacity()
capa1.SprintID = 1
capa1.MemberID = 1
capa1.CapacityDays = 40
capa1.MissingDays = 0
capa1.CreatedByID = 5
capa1.CreationDate = dt_string
capa1.LastUpdate = dt_string
capa1.save()

capa2 = Capacity()
capa2.SprintID = 2
capa2.MemberID = 1
capa2.CapacityDays = 30
capa2.MissingDays = 10
capa1.CreatedByID = 5
capa2.CreationDate = dt_string
capa2.LastUpdate = dt_string
capa2.save()

disconnect()
