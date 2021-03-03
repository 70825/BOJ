def Post(preorder,inorder):
    t=len(preorder)
    if t==0:return
    root=preorder[0]
    for i in range(t):
        if inorder[i]==root:
            L=i;break
    R=t-L-1
    Post(preorder[1:L+1],inorder[0:L])
    Post(preorder[L+1:t],inorder[L+1:t])
    print(root,end=" ")

for _ in range(int(input())):
    n=int(input())
    Pre=[*map(int,input().split())]
    In=[*map(int,input().split())]
    Post(Pre,In)
    print()