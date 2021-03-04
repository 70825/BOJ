#include <bits/stdc++.h>
using namespace std;
const int MAX=200000;
int Max=1000002;
vector<pair<int,int>> path[MAX];
struct HK {
    vector<int> A,B,used,level;
    int n,m;
    HK(int a, int b){
        A.resize(MAX,-1);
        B.resize(MAX*2,-1);
        used.resize(MAX,0);
        level.resize(MAX,0);
        n=a;m=b;
    }
    void bfs() {
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (used[i] == 0) {
                level[i] = 0;
                q.push(i);
            }
            else level[i] = Max;
        }
        while (!q.empty()) {
            int x = q.front();q.pop();
            for (auto &N: path[x]) {
                int nx = N.second;
                if (B[nx] != -1 && level[B[nx]] == Max) {
                    level[B[nx]] = level[x] + 1;
                    q.push(B[nx]);
                }
            }
        }
    }

    int dfs(int x) {
        for (auto &N: path[x]) {
            int nt = N.first, nx = N.second;
            if (nt > m) break;
            if (B[nx] == -1 || (level[B[nx]] == level[x] + 1 && dfs(B[nx]))) {
                used[x] = 1;
                A[x] = nx;
                B[nx] = x;
                return 1;
            }
        }
        return 0;
    }
};
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n,a,b,c,d;
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> a >> b >> c >> d;
        if(b>d){
            swap(a,c);
            swap(b,d);
        }
        path[i].push_back(make_pair(b,a-1));
        path[i].push_back(make_pair(d,c-1));
    }
    int l=0,r=Max,m;
    while(l<=r){
        m=(l+r)/2;
        HK H(n,m);
        int match=0;
        while(true){
            H.bfs();
            int flow=0;
            for(int i=0; i<n; i++){
                if(H.used[i]==0 && H.dfs(i)) flow+=1;
            }
            if(flow==0) break;
            match+=flow;
        }
        if(match!=n) l=m+1;
        else r=m-1;
    }
    if(l>=Max) cout << -1 << "\n";
    else cout << l << "\n";
}