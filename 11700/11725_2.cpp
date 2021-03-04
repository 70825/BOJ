#include <bits/stdc++.h>
using namespace std;

vector<int> parent;
vector<vector<int>> adj;

void DFS(int x, int prev){
    for(auto nx: adj[x]){
        if(parent[nx] == -1 && nx!=prev){
            parent[nx] = x;
            DFS(nx,x);
        }
    }
}

int main(){
    cin.sync_with_stdio(false);
    cin.tie(NULL);
    int n,x,y;
    cin >> n;

    parent.resize(n, -1);
    adj.resize(n);

    for(int i=1; i<n; i++){
        cin >> x >> y;
        x--;y--;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }

    DFS(0,-1);

    for(int i=1; i<n; i++){
        cout << parent[i] + 1 << "\n";
    }
}