a,b,c,d = map(int,input().split())
flag = 0
for i in range(d//a+1):
    for j in range((d-a*i)//b+1):
        for k in range((d-a*i-b*j)//c+1):
            if a*i + b*j + c*k == d: flag = 1
print(flag)
