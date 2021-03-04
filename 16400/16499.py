T=int(input())
D=[]
for i in range(T):
    s=str(input());k=[]
    for j in range(len(s)):
        if 0<=ord(s[j])-97<=25:k.append(s[j])
        k.sort()
    if k in D:continue
    else:D.append(k)
print(len(D))