input=__import__('sys').stdin.readline
for i in range(int(input())):
    N=int(bin(int(input()))[2::])
    if N&-N==int(str(N),2):print(1)
    else:print(0)