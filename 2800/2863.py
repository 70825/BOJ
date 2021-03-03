A,B=map(int,input().split())
C,D=map(int,input().split())
memo=[A/C+B/D,C/D+A/B,D/B+C/A,B/A+D/C]
for i in range(len(memo)):
    if max(memo)==memo[i]:print(i)