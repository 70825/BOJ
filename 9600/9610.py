N = int(input())
A=0;B=0;C=0;D=0;E=0
for i in range(N):
    x,y = map(int,input().split())
    if x>0 and y>0:
        A+=1
    elif x<0 and y>0:
        B+=1
    elif x<0 and y<0:
        C+=1
    elif x>0 and y<0:
        D+=1
    else:
        E+=1
print("Q1:",A)
print("Q2:",B)
print("Q3:",C)
print("Q4:",D)
print("AXIS:",E)