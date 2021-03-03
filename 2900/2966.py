N = int(input())
Adrian_ = [None] * N
Bruno_ = [None] * N
Goran_ = [None] * N
Adrian = 0
Bruno = 0
Goran = 0


def A_Adrian(x):
    for i in range(x):
        if (i+1) % 3 == 1:
            Adrian_[i] = 'A'
        elif (i+1) % 3 == 2:
            Adrian_[i] = 'B'
        else:
            Adrian_[i] = 'C'
def A_Bruno(x):
    for i in range(x):
        if (i+1) % 4 == 1 or (i+1) % 4 == 3:
            Bruno_[i] = 'B'
        elif (i+1) % 4 == 2:
            Bruno_[i] = 'A'
        else:
            Bruno_[i] = 'C'

def A_Goran(x):
    for i in range(x):
        if 1<= (i+1) % 6 <= 2:
            Goran_[i] = 'C'
        elif 3<= (i+1) % 6 <=4:
            Goran_[i] = 'A'
        else:
            Goran_[i] = 'B'
if 1<= N <= 100:
    answer = str(input())
    answer.split()
    A_Adrian(N)
    A_Bruno(N)
    A_Goran(N)
    for i in range(N):
        if Adrian_[i] == answer[i]:
            Adrian += 1
        if Bruno_[i] == answer[i]:
            Bruno += 1
        if Goran_[i] == answer[i]:
            Goran += 1
    print(max(Adrian,Bruno,Goran))
    if Adrian == Bruno == Goran:
        print("Adrian Bruno Goran")
    elif Adrian == Bruno > Goran :
        print("Adrian Bruno")
    elif Adrian == Goran > Bruno :
        print("Adrian Goran")
    elif Bruno == Goran > Adrian:
        print("Bruno Goran")
    elif max(Adrian,Bruno,Goran) == Adrian:
        print("Adrian")
    elif max(Adrian,Bruno,Goran) == Bruno:
        print("Bruno")
    elif max(Adrian,Bruno,Goran) == Goran:
        print("Goran")