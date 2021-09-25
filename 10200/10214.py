for _ in range(int(input())):
    score = [[*map(int, input().split())] for _ in range(9)]
    y = sum(score[i][0] for i in range(9))
    k = sum(score[i][1] for i in range(9))

    if y > k: print('Yonsei')
    elif k > y: print('Korea')
    else: print('Draw')