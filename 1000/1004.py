from math import sqrt
for i in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    s_planet=[]
    e_planet=[]
    for j in range(n):
        Cx,Cy,r=map(int,input().split())
        if sqrt((x1-Cx)**2+(y1-Cy)**2)>r:s_planet.append(0)
        else:s_planet.append(1)
        if sqrt((x2-Cx)**2+(y2-Cy)**2)>r:e_planet.append(0)
        else:e_planet.append(1)
    result=0
    for j in range(n):
        if s_planet[j]!=e_planet[j]:result+=1
    print(result)