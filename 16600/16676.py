N=str(input())
if N=='0':print(1)
elif int(N)<int('1'*len(N)):print(len(N)-1)
else:print(len(N))