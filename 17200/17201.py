N=int(input())
a=input()
err=0
for i in range(1,len(a)-1,2):
    if a[i]==a[i+1]:err+=1
print(['Yes','No'][err!=0])