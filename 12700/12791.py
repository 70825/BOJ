D=[[1967,'DavidBowie'],[1969,'SpaceOddity'],[1970, 'TheManWhoSoldTheWorld'],
[1971, 'HunkyDory'],[1972, 'TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars'],
[1973, 'AladdinSane'],[1973, 'PinUps'],[1974, 'DiamondDogs'],[1975, 'YoungAmericans'],
[1976, 'StationToStation'],[1977, 'Low'],[1977, 'Heroes'],[1979, 'Lodger'],
[1980, 'ScaryMonstersAndSuperCreeps'],[1983, 'LetsDance'],[1984, 'Tonight'],
[1987, 'NeverLetMeDown'],[1993, 'BlackTieWhiteNoise'],[1995, '1.Outside'],
[1997, 'Earthling'],[1999, 'Hours'],[2002, 'Heathen'],[2003, 'Reality'],
[2013, 'TheNextDay'],[2016, 'BlackStar']]

for i in range(int(input())):
    S,E=map(int,input().split())
    memo=[]
    for j in D:
        if S<=j[0]<=E:
            memo.append(j)
    print(len(memo))
    for j in range(len(memo)):
        print(memo[j][0],memo[j][1])
