a,b,c,d,e=map(str,input().split());s=[]
def k(x,y,z):
    x=int(x);z=int(z)
    if y=='+':return x+z
    elif y=='-':return x-z
    elif y=='*':
        if (x<0 and z<0) or (x>0 and z>0):return x*z
        else:return -(abs(x)*abs(z))
    elif y=='/':
        if (x < 0 and z < 0) or (x > 0 and z > 0):return x//z
        else:return -(abs(x)//abs(z))
s.append(k(k(a,b,c),d,e))
s.append(k(a,b,k(c,d,e)))
s.sort()
for i in range(2):
    print(s[i])