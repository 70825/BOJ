s = input()
D = []
minus = []
z = []
for i in range(len(s)):
    if s[i] in '-+':
        D.append(int(''.join(z)));z=[]
        if s[i] == '-': minus.append(len(D))
    else:z.append(s[i])
else:D.append(int(''.join(z)))
if len(minus)==0:print(sum(D))
elif len(minus)==1:print(sum(D[:minus[0]])-sum(D[minus[0]:]))
else:
    ans = sum(D[:minus[0]])
    for i in range(1,len(minus)):
        ans -= sum(D[minus[i-1]:minus[i]])
    ans -= sum(D[minus[len(minus)-1]:])
    print(ans)