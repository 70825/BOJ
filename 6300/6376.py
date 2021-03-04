from fractions import Fraction
print('n e')
print('- -----------')
for i in range(1,11):
    s=0
    for j in range(i):
        ans=1
        for k in range(j):
            ans*=k+1
        s+=Fraction(1,ans)
    if int(s)==float(s):print(i-1,int(s))
    elif i==3:print(i-1,round(float(s),9))
    else:print(i-1,"{0:.9f}".format(float(s)))