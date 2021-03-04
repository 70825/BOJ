p=int(input())
D=['B']*(101)
def Color():
    if D[j]=='B':D[j]='R'
    elif D[j]=='R':D[j]='G'
    else:D[j]='B'
for i in range(int(input())):
    x,y=map(str,input().split());x=int(x)
    if y=='R':
        for j in range(x+1,101):Color()
    else:
        for j in range(x-1,0,-1):Color()
r,g,b=0,0,0
for i in range(1,101):
    if D[i]=='B':b+=1
    elif D[i]=='G':g+=1
    else:r+=1
print('{0:.2f}'.format(b/100*p))
print('{0:.2f}'.format(r/100*p))
print('{0:.2f}'.format(g/100*p))