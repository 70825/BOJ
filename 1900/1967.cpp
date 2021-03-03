#include <bits/stdc++.h>
using namespace std;

vector<vector<pair<int,int>>> adj;
queue<int> leaf;
int ans = 0;

void connect_node(int x, int y, int z){
    adj[x].push_back(make_pair(y,z));
    adj[y].push_back(make_pair(x,z));
}

void find_leaf(){
    queue<int> q;
    int visited[10001];
    memset(visited,0,sizeof(visited));

    q.push(0);
    visited[0] = 1;
    while(!q.empty()){
        int x = q.front(); q.pop();
        for(auto z: adj[x]){
            int nx = z.first;
            if(!visited[nx]) {
                if (adj[nx].size() == 1) leaf.push(nx);
                visited[nx] = 1;
                q.push(nx);
            }
        }
    }
}

void BFS(int z){
    int S[10001];
    memset(S,-1,sizeof(S));

    queue<int> q;
    q.push(z);
    S[z] = 0;
    while(!q.empty()){
        int x = q.front(); q.pop();
        for(auto k: adj[x]){
            int nx = k.first;
            int ny = k.second;
            if(S[nx] == -1){
                S[nx] = S[x] + ny;
                if(S[nx] > ans) ans = S[nx];
                q.push(nx);
            }
        }
    }
}

int main(){
    int n,x,y,z;
    cin >> n;
    adj.resize(n);
    for(int i=0; i<n-1; i++){
        cin >> x >> y >> z;
        connect_node(x-1,y-1,z);
    }
    find_leaf();
    while(!leaf.empty()){
        x = leaf.front(); leaf.pop();
        BFS(x);
    }
    cout << ans;
}