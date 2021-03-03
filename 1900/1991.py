def Preorder(x):
    print(chr(x+65),end='')
    if Left_Children[x]!=-1: Preorder(Left_Children[x])
    if Right_Childeren[x]!=-1:Preorder(Right_Childeren[x])
def Inorder(x):
    if Left_Children[x]!=-1: Inorder(Left_Children[x])
    print(chr(x+65),end='')
    if Right_Childeren[x]!=-1: Inorder(Right_Childeren[x])
def Postorder(x):
    if Left_Children[x]!=-1:Postorder(Left_Children[x])
    if Right_Childeren[x]!=-1:Postorder(Right_Childeren[x])
    print(chr(x+65),end='')
n=int(input())
Left_Children=[-1]*n
Right_Childeren=[-1]*n
for i in range(n):
    a,b,c=input().split()
    if b!='.':Left_Children[ord(a)-65]=ord(b)-65
    if c!='.':Right_Childeren[ord(a)-65]=ord(c)-65
Preorder(0)
print('')
Inorder(0)
print('')
Postorder(0)