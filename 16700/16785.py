A,B,C=map(int,input().split())
day=0
while C>0:
    if C>6*A:C-=A*7+B;day+=7
    else:C-=A;day+=1
print(day)