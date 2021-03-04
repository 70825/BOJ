n=int(input())
sum=0
ans=1
while 1:
    sum+=ans**2+(ans-1)**2
    if n<sum:print(ans-1);break
    elif n==sum:print(ans);break
    else:ans+=1