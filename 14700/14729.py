input=__import__('sys').stdin.readline
D=[]
for _ in range(int(input())):D.append(float(input()))
D=sorted(D)[:7]
for i in range(7):print('{0:.3f}'.format(D[i]))