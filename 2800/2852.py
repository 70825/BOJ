team = [0, 0]
score = [0, 0]

time = 0
n = int(input())
for i in range(n):
    a, b = input().split()
    a = int(a)
    b, c = map(int,b.split(':'))

    x = 60*b + c
    if score[0] > score[1]: team[0] += x - time
    elif score[0] < score[1]: team[1] += x - time
    time = x

    if a == 1: score[0] += 1
    else: score[1] += 1
if score[0] > score[1]: team[0] += 48*60 - time
elif score[0] < score[1]: team[1] += 48*60 - time

for i in range(2):
    m = str(team[i]//60)
    s = str(team[i]%60)
    print('0'*(2-len(m)) + m + ':' + '0'*(2-len(s)) + s)