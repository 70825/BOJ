S1,S2=map(int,input().split())
s1,s2=0,0
for i in range(S1):
    a,b=map(int,input().split())
    if a==b:s1+=1
for i in range(S2):
    a,b=map(int,input().split())
    if a==b:s2+=1
if s1==S1 and s2==S2:
    print('Accepted')
elif s1==S1 and s2!=S2:
    print('Why Wrong!!!')
else:
    print('Wrong Answer')