#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;

int main(){
    int n;
    cin >> n;
    int nm=2*(n+1);
    int c[nm][nm],d[nm][nm],f[nm][nm],t[n][n],S=nm-2,E=nm-1;
    memset(c,0,sizeof(c));
    memset(d,0,sizeof(d));
    memset(f,0,sizeof(f));
    memset(t,0,sizeof(t));
    vector<int> path[nm];
    for(int i=0; i<n; i++){
        c[S][i]=1;
        path[i].push_back(S);
        path[S].push_back(i);
        c[i+n][E]=1;
        path[i+n].push_back(E);
        path[E].push_back(i+n);
        for(int j=0; j<n; j++){
            cin >> t[i][j];
            c[i][j+n]=1;
            d[i][j+n]=t[i][j];
            d[j+n][i]=-t[i][j];
            path[i].push_back(j+n);
            path[j+n].push_back(i);
        }
    }
    int cost=0;
    while(true){
        queue<int> q;
        q.push(S);
        int inQ[nm],dist[nm],prev[nm];
        fill(inQ,inQ+nm,0);
        fill(dist,dist+nm,INF);
        fill(prev,prev+nm,-1);
        dist[S]=0;
        inQ[S]=1;
        while(!q.empty()){
            int x=q.front();q.pop();
            inQ[x]=0;
            for(auto nx: path[x]){
                if(c[x][nx]-f[x][nx]>0 && dist[nx]>dist[x]+d[x][nx]){
                    dist[nx]=dist[x]+d[x][nx];
                    prev[nx]=x;
                    if(inQ[nx]==0){
                        q.push(nx);
                        inQ[nx]=1;
                    }
                }
            }
        }
        if(prev[E]==-1) break;
        int x=E;
        while(x!=S){
            int nx=prev[x];
            f[nx][x]+=1;
            f[x][nx]-=1;
            cost+=d[nx][x];
            x=nx;
        }
    }
    cout << cost << endl;
}