input=__import__('sys').stdin.readline
a=[0]*20
for i in range(int(input())):
    M=input().split()
    if len(M)==2:M[1]=int(M[1])-1
    if M[0]=='all':a=[1]*20
    elif M[0]=='empty':a=[0]*20
    elif M[0]=='add':
        if a[M[1]]==0:a[M[1]]=1
    elif M[0]=='remove':
        if a[M[1]]==1:a[M[1]]=0
    elif M[0]=='check':
        if a[M[1]]==1:print(1)
        else:print(0)
    elif M[0]=='toggle':
        if a[M[1]]==1:a[M[1]]=0
        else:a[M[1]]=1