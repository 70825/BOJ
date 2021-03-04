#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> adj;
vector<int> val;
vector<int> visited;

int DFS(int x, int prev){
    for(auto nx: adj[x]){
        if(!visited[nx] && nx != prev){
            visited[nx] = 1;
            val[x] += DFS(nx, x);
        }
    }
    return val[x];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n,r,q,u,v,x;
    cin >> n >> r >> q;
    r--;

    adj.resize(n);
    val.resize(n,1);
    visited.resize(n,0);

    for(int i=1; i<n; i++){
        cin >> u >> v;
        u--;v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    visited[r] = 1;
    DFS(r, -1);
    for(int i=0; i<q; i++){
        cin >> x; x--;
        cout << val[x] << "\n";
    }
}