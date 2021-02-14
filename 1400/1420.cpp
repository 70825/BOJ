#include <bits/stdc++.h>
using namespace std;

const int INF=1e9;
const int nm=20002;
char D[101][101];
vector<int> path[nm];
map<pair<int,int>,int> c;
map<pair<int,int>,int> f;


void edge(int x, int y, int z){
    c[make_pair(x,y)]=z;
    c[make_pair(y,x)]=0;
    path[x].push_back(y);
    path[y].push_back(x);
}

int main(){
    int n,m;
    cin >> n >> m;
    int S=-1,E=-1,sx=-1,sy=-1,ex=-1,ey=-1;
    int cnt=0;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> D[i][j];
            if(D[i][j]=='K'){
                S=cnt+1;
                sx=i;
                sy=j;
            }
            if(D[i][j]=='H'){
                E=cnt;
                ex=i;
                ey=j;
            }
            cnt+=2;
        }
    }
    if(n==1 && m==1){
        cout << -1;
        return 0;
    }
    if(S==-1 || E==-1){
        cout << -1;
        return 0;
    }
    if(abs(sx-ex)+abs(sy-ey)==1){
        cout << -1;
        return 0;
    }
    for(int i=0;i<n*m;i++){
        edge(i*2,i*2+1,1);
    }
    int t=0;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(i+1 < n && D[i][j] != '#' && D[i+1][j] != '#'){
                int nt = t + 2 * m;
                edge(t+1, nt, INF);
                edge(nt+1, t, INF);
            }
            if(j+1 < m && D[i][j] != '#' && D[i][j+1] != '#'){
                int nt = t + 2;
                edge(t+1, nt, INF);
                edge(nt+1, t, INF);
            }
            t+=2;
        }
    }
    int res=0;
    while(true){
        queue<int> q;
        q.push(S);
        int prev[nm];
        fill(prev,prev+nm,-1);
        while(!q.empty()){
            int x=q.front();q.pop();
            for(auto nx:path[x]){
                if(c[make_pair(x,nx)]-f[make_pair(x,nx)]>0 && prev[nx]==-1){
                    prev[nx]=x;
                    q.push(nx);
                }
            }
        }
        if(prev[E]==-1)break;
        int x=E;
        while(x!=S){
            int nx=prev[x];
            f[make_pair(nx,x)]+=1;
            f[make_pair(x,nx)]-=1;
            x=nx;
        }
        res+=1;
    }
    cout << res;
    return 0;
}