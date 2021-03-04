K = str(input())
if len(K) <= 10000 and K == K.upper():
    ioi = 0
    joi = 0
    for i in range(len(K)-2):
        if K[i]+K[i+1]+K[i+2] == "JOI":
            joi += 1
        elif K[i]+K[i+1]+K[i+2] == "IOI":
            ioi += 1
    print(joi)
    print(ioi)