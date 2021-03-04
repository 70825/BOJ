s=input();k=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:k+=1
print(['Odd.','Or not.'][k>0])