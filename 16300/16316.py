input();err=0
D=input().split()
for i in range(len(D)):
    if D[i]!='mumble' and int(D[i])!=i+1:err+=1
print(['something is fishy','makes sense'][err==0])