import sys
D=[]
for i in range(int(input())):
    D.append(int(sys.stdin.readline()))
D.sort(reverse=True)
print('\n'.join(map(str,D)))