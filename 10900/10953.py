T = int(input())
for i in range(T):
    A,B = input().split(',')
    if 0<int(A)<10 and 0<int(B)<10:
        print(int(A)+int(B))