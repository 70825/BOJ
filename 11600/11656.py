k=[*input()][::-1]
a='';D=[]
for i in range(len(k)):
    a+=k[i]
    D.append(a[::-1])
for x in sorted(D):print(x)