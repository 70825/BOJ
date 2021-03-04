n,m,q=map(int,input().split())
# n은 팀의 수, m은 문제 수
Team_score=[0]*n
Team_problem=[0]*n
Team_solve=[[] for _ in range(n)]
Team_wrong=[[0]*m for _ in range(n)]
for i in range(q):
    A,B,C,D = input().split()
    A = int(A);B = int(B);C = int(C)
    # A는 경과시간, B는 팀번호, C는 문제번호, D는 채점결과
    if C not in Team_solve[B-1]:
        if D=='AC':
            Team_solve[B-1].append(C)
            Team_score[B-1]+=A+Team_wrong[B-1][C-1]*20
            Team_problem[B-1]+=1
        else:
            Team_wrong[B-1][C-1]+=1
problem=sorted(list(set(Team_problem)),reverse=True)
for i in range(len(problem)):
    K=[]
    for j in range(len(Team_problem)):
        if Team_problem[j]==problem[0]:
            K.append([Team_score[j],j+1])
    K.sort()
    for j in range(len(K)):
        print(K[j][1],problem[0],K[j][0])
    problem.pop(0)