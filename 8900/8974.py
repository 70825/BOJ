A,B=map(int,input().split())
k=1
a,b=0,0
while 1:
    if k*(k-1)//2<A<=k*(k+1)//2:a=k-1
    if k*(k-1)//2<B<=k*(k+1)//2:b=k-1
    if k*(k+1)//2>=B:break
    k+=1
sum_A=a*(a+1)*(2*a+1)//6+(a+1)*(A-a*(a+1)//2)
sum_B=b*(b+1)*(2*b+1)//6+(b+1)*(B-b*(b+1)//2)
print(sum_B-sum_A+a+1)