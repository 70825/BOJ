N = int(input())
k = [1] * N
total = [0] * N

for i in range(N):
    k[i] = str(input())
    score = [0] * len(k[i])
    k[i].split(':')
    for j in range(len(k[i])):
        if j == 0 and k[i][j] == 'O':
            score[0] = 1
            total[i] += score[0]
        elif k[i][j] == 'X':
            score[j] = 0
        elif j >= 1 and k[i][j] == 'O':
            score[j] = score[j-1] + 1
            total[i] += score[j]
    print(total[i])