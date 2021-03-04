m,n=map(int,input().split());i=0;a=[]
b=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
if m==0:print(0)
else:
    while m!=0:
        a.insert(0,b[m%n])
        m//=n
    for i in range(len(a)):
        print(a[i],end="")