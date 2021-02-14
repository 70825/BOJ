N=int(input())
memo=[*map(int,input().split())]
print(max(memo)*min(memo))