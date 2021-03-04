X=[];Y=[]
for i in range(3):
    x,y=map(int,input().split())
    X.append(x);Y.append(y)
if len(set(X))==1 or len(set(Y))==1:print('WHERE IS MY CHICKEN?')
elif len(set(X))==2 or len(set(Y))==2:print('WINNER WINNER CHICKEN DINNER!')
else:
    a=(X[2]-X[1])/(Y[2]-Y[1])
    b=(X[1]-X[0])/(Y[1]-Y[0])
    if a==b:print('WHERE IS MY CHICKEN?')
    else:print('WINNER WINNER CHICKEN DINNER!')