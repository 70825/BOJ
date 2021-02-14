import math
def find_num(N):
    x1, y1, r1, x2, y2, r2 = map(int,N.split(' '))
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    r_sum = r1+r2
    if distance == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if distance > r_sum:
            print(0)
        elif distance == r_sum:
            print(1)
        elif distance < r_sum:
            if (distance+min(r1,r2)) == max(r1,r2):
                print(1)
            elif(distance+min(r1,r2)) < max(r1,r2):
                print(0)
            else:
                print(2)

trials = int(input())
input_data = []

for i in range(trials):
    N = input()
    find_num(N)