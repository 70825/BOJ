#include <bits/stdc++.h>
using namespace std;
#define MAX 1000001
vector<int> adj[MAX];
int ans[MAX][2];

void make_node(int x, int y){
    adj[x].push_back(y);
    adj[y].push_back(x);
}

int DFS(int x, int ea, int prev){
    if(ans[x][ea] != -1) return ans[x][ea];
    if(ea) ans[x][ea] = 1;
    else ans[x][ea] = 0;
    for(auto nx: adj[x]){
        if(nx != prev)
        {
            if(ea) ans[x][ea] += min(DFS(nx,0,x),DFS(nx,1,x));
            else ans[x][ea] += DFS(nx,1,x);
        }
    }
    return ans[x][ea];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n,u,v;

    cin >> n;
    for(int i=1; i<n; i++){
        cin >> u >> v;
        make_node(--u,--v);
    }

    memset(ans,-1,sizeof(ans));

    cout << min(DFS(0,0,-1),DFS(0,1,-1));
}