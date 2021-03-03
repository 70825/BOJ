M=input().split();s=''
D=['i','pa','te','ni','niti','a','ali','nego','no','ili']
for i in range(len(M)):
    if M[i] in D and i>0:continue
    else:s+=M[i][0].upper()
print(s)