infile = open("WorldSeriesWinners.txt", "r")

world_series_teams = dict()

for team in infile:
    if team in world_series_teams:
        world_series_teams[team] += 1
        team.strip("\n")
    else:
        world_series_teams[team] = 1
        team.strip("\n")


infile.close()



infile = open("WorldSeriesWinners.txt", "r")

world_series_years = dict()

year = 1903
for team in infile:
    if year == 1904 or year == 1994: 
        year +=1
    world_series_years[year] = team
    year += 1


year_choice = int(input('What year would you like to see? '))

print(str(year_choice) + ': ' + world_series_years[year_choice] + str(world_series_teams[world_series_years[year_choice]]) + ' World Series Win(s)')

