#include <bits/stdc++.h>
using namespace std;

class Tree{
private:
    int N;
    vector<int> parent;
    vector<vector<int>> children;
    vector<vector<int>> adj;
    vector<long long> value;
    vector<bool> visited;
public:
    Tree():N(0){}
    Tree(int n):N(n){
        parent.resize(N,-1);
        children.resize(N);
        adj.resize(N);
        value.resize(N,0);
        visited.resize(N,false);
    }
    void make_land(int a, long long b, int c){
        adj[a].push_back(c);
        adj[c].push_back(a);
        value[a] = b;
    }


    void make_tree(){
        queue<int> q;
        q.push(0);
        visited[0] = true;
        while(!q.empty()){
            int x = q.front();q.pop();
            for(auto nx: adj[x]){
                if(!visited[nx]){
                    visited[nx] = true;
                    q.push(nx);
                    parent[nx] = x;
                    children[x].push_back(nx);
                }
            }
        }
    }

    long long resque(int x){
        for(auto nx: children[x]){
            value[x]+=resque(nx);
        }
        if(value[x] < 0) return 0;
        return value[x];
    }

};

int main(){
    int n,z;
    long long y;
    char x;

    cin >> n;
    Tree T(n);

    for(int i=1; i<n; i++){
        cin >> x >> y >> z;
        if(x=='S') T.make_land(i,y,z-1);
        else T.make_land(i,-y,z-1);
    }

    T.make_tree();
    
    cout << T.resque(0) << endl;
}