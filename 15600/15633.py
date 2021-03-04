A=int(input());d=0
for i in range(1,A+1,1):
    if int(A/i)==A/i:
        d+=i
print(d*5-24)