arr = list(map(int,input().split()))
score = int(input())
arr = sorted(arr)

rank = 0
for i in range(len(arr)):
    if arr[i] == score: rank = len(arr) - i

if rank <= 5: print('A+')
elif rank <= 15: print('A0')
elif rank <= 30: print('B+')
elif rank <= 35: print('B0')
elif rank <= 45: print('C+')
elif rank <= 48: print('C0')
else:print('F')