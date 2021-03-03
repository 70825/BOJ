for i in range(int(input())):
    a=[[0,0] for j in range(4)]
    D=[];z=0
    for j in range(4):
        x,y=map(int,input().split())
        a[j][0]=x;a[j][1]=y
    for j in range(3):
        for k in range(j+1,4,1):
            D.append((a[j][0]-a[k][0])**2+(a[j][1]-a[k][1])**2)
    D=list(set(D))
    if len(D)==2:print(1)
    else:print(0)