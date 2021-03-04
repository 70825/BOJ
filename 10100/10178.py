T = int(input())
for i in range(T):
    F = input()
    x,y = F.split(' ')
    print("You get",int(int(x)/int(y)),"piece(s) and your dad gets",int(int(x)%int(y)),"piece(s).")