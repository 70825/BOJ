#include <bits/stdc++.h>
using namespace std;

vector<int> val;
vector<vector<int>> adj;
int visited[10001];
long long ans[10001][2];

void connect(int x, int y){
    adj[x].push_back(y);
    adj[y].push_back(x);
}

long long DFS(int x, int y, int prev){
    if(ans[x][y] != -1) return ans[x][y];
    if(y) ans[x][y] = val[x];
    else ans[x][y] = 0;
    for(auto nx: adj[x]){
        if(nx != prev) {
            if (y) ans[x][1] += DFS(nx, 0, x);
            else ans[x][0] += max(DFS(nx, 0, x), DFS(nx, 1, x));
        }
    }
    return ans[x][y];
}

int main(){
    int n, x, y;
    cin >> n;

    val.resize(n,0);
    adj.resize(n);
    memset(ans,-1,sizeof(ans));

    for(int i=0; i<n; i++) cin >> val[i];

    for(int i=1; i<n; i++){
        cin >> x >> y;
        connect(--x,--y);
    }
    cout << max(DFS(0,0,-1),DFS(0,1,-1));
}