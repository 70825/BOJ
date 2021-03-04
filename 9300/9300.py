from math import *
for i in range(int(input())):
    h, t = map(float, input().split())
    t = radians(t)
    print('Case '+str(i+1)+':',end=" ")
    if tan(t)==0:print(0.00)
    else:print(abs(round(h * (1 - tan(t)) / tan(t), 5)))