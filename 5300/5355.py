T=int(input())
for i in range(T):
    a=input().split()
    a[0]=float(a[0])
    for j in range(1,len(a)):
        if a[j]=='@':a[0]*=3
        elif a[j]=='%':a[0]+=5
        elif a[j]=='#':a[0]-=7
    a[0]=round(a[0],2)
    print("{0:.2f}".format(a[0]))