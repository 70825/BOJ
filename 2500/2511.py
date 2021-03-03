A=list(map(int,input().split()));a=0;b=0;d=0
B=list(map(int,input().split()))
for i in range(10):
    if A[i]>B[i]:a+=3
    elif A[i]<B[i]:b+=3
    else:a+=1;b+=1;d+=1
print(a,b)
if a>b:print('A')
elif b>a:print('B')
else:
    if d==10:print('D')
    else:
        for i in range(9,-1,-1):
            if A[i]>B[i]:print('A');break
            elif B[i]>A[i]:print('B');break