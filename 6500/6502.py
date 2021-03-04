c = 1
while True:
    A = input()
    if A[0]=='0':break
    R,W,L=map(int,A.split())
    if W**2+L**2 <= (2*R)**2:print("Pizza %d fits on the table."%c)
    else:print("Pizza %d does not fit on the table."%c)
    c+=1