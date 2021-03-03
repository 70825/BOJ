#include <bits/stdc++.h>
using namespace std;
int t = 0;
int m[101][101] = {0};
int apple[101][101] = {0};
int nxny[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
int dir = 0;
pair<int, char>p;
queue<pair<int, char>> q;


class Node{
    friend class doubly_linked_list;
public:
    int x;
    int y;
    Node *next;
    Node *prev;
    Node(int x, int y, Node *n,Node *p):x(x),y(y),next(n),prev(p){};
};

class doubly_linked_list{
public:
    Node *head;
    Node *tail;
    doubly_linked_list(){
        Node *new_node = new Node(0,0,nullptr,nullptr);
        head = tail = new_node;
        m[0][0] = 1;
    }
    void move(){
        Node *dest = tail;
        m[tail->x][tail->y] = 0;
        do{
            if(dest == head){
                dest -> x = dest -> x + nxny[dir][0];
                dest -> y = dest -> y + nxny[dir][1];
            }
            else {
                dest-> x = dest-> prev -> x;
                dest-> y = dest-> prev -> y;
            }
            m[dest->x][dest->y] = 1;
            dest = dest -> prev;
        }while(dest != nullptr);
    }

    void eat_apple(int x, int y){
        Node *new_node = new Node(x,y,nullptr,nullptr);
        new_node -> next = head;
        head -> prev = new_node;
        head = new_node;
        m[x][y] = 1;
        apple[x][y] = 0;
    }
};

int main(){
    int n,k,x,y,l;
    char a;

    doubly_linked_list DLL;

    cin >> n;
    cin >> k;
    for(int i=0; i<k; i++){
        cin >> x >> y;
        apple[x-1][y-1] = 1;
    }
    cin >> l;
    for(int i=0; i<l; i++){
        cin >> x >> a;
        q.push(make_pair(x,a));
    }
    q.push(make_pair(99999,'D'));

    while(1){
        int nx, ny, nt;
        char nd;
        nx = DLL.head -> x + nxny[dir][0];
        ny = DLL.head -> y + nxny[dir][1];
        p = q.front();
        nt = p.first;
        nd = p.second;

        if(nx<0 || nx>=n || ny<0 || ny>=n || m[nx][ny]==1){
            cout << t+1 << endl;
            break;
        }
        else if(apple[nx][ny] == 1) DLL.eat_apple(nx,ny);
        else DLL.move();

        t++;
        if(t == nt){
            if(nd == 'D') dir = (dir+1)%4;
            else dir = (dir+3)%4;
            q.pop();
        }
    }

    return 0;
}