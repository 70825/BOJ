A,B,C,D=map(int,input().split());P= [0,0,0]
P[0],P[1],P[2]=map(int,input().split())
a=A+B
b=C+D
for i in range(3):
    if (P[i]%a!=0 and P[i]%a<=A) and (P[i]%b!=0 and P[i]%b<=C):print(2)
    elif (P[i]%a!=0 and P[i]%a<=A) or (P[i]%b!=0 and P[i]%b<=C):print(1)
    else:print(0)