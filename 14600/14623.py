m=input()
n=input()
a=bin(int(m,2)*int(n,2))
for i in range(2,len(a)):print(a[i],end="")