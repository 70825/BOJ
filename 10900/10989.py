input=__import__('sys').stdin.readline
D=[0]*10001
for _ in range(int(input())):
    D[int(input())]+=1
for i in range(1,10001):
    print('{}\n'.format(i)*D[i],end='')