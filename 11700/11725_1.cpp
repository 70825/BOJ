#include <bits/stdc++.h>
using namespace std;

class Tree{
private:
    int N;
    vector<int> parent;
    vector<vector<int>> adj;
    vector<bool> visited;
public:
    Tree(): N(0){}
    Tree(int n): N(n){
        parent.resize(N,-1);
        adj.resize(N);
        visited.resize(N,false);
    }
    void connect_node(int x, int y){
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    void find_parent(){
        queue<int> q;
        q.push(0);
        visited[0] = true;
        while(!q.empty()){
            int x = q.front(); q.pop();
            for(int nx: adj[x]){
                if(!visited[nx]){
                    visited[nx] = true;
                    q.push(nx);
                    parent[nx] = x;
                }
            }
        }
    }
    void print(int x){
        printf("%d\n",parent[x]+1);
    }
};

int main(){
    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    int n,x,y;

    cin >> n;
    Tree T(n);

    for(int i=0; i<n-1; i++){
        cin >> x >> y;
        T.connect_node(x-1,y-1);
    }
    T.find_parent();
    for(int i=1; i<n; i++) T.print(i);

    return 0;
}
