Array=[*input()]
C=10;D=26
if Array[0]=='d':ans=10;Type=['d',9]
else:ans=26;Type=['c',25]
for i in range(1,len(Array)):
    if Array[i]=='d':
        if Type[0]=='d':ans*=Type[1]
        else:ans*=10;Type=['d',9]
    else:
        if Type[0]=='c':ans*=Type[1]
        else:ans*=26;Type=['c',25]
print(ans)