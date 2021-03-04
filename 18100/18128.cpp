#include <bits/stdc++.h>
using namespace std;

queue<pair<int,int>>q;
queue<pair<int,int>>water_q;
pair<int,int>p;
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};
int kx[8]={-1,-1,-1,0,0,1,1,1};
int ky[8]={-1,0,1,-1,1,-1,0,1};
int n,w,a,b,x,y,t,nx,ny,nt,i,j;
char D[1001][1001];
int check[1001][1001];
int water_check[1001][1001];
int INF=987654321;

int main(){
    memset(D,0,sizeof(D));
    memset(check,-1,sizeof(check));
    memset(water_check,-1,sizeof(water_check));
    cin >> n >> w;
    for(i = 0; i < w; i++){
        cin >> a >> b;
        water_q.push(make_pair(a-1,b-1));
        water_check[a-1][b-1]=0;
    }
    for(i = 0; i < n; i++){
        scanf("%s",&D[i]);
    }
    while(!water_q.empty()){
        p = water_q.front();water_q.pop();
        x = p.first;
        y = p.second;
        t = water_check[x][y];
        for(i = 0; i < 4; i++){
            nx = x+dx[i];
            ny = y+dy[i];
            if(0<=nx && nx<n && 0<=ny && ny<n && water_check[nx][ny]==-1){
                water_check[nx][ny]=t+1;
                water_q.push(make_pair(nx,ny));
            }
        }
    }
    q.push(make_pair(0,0));
    while(!q.empty()){
        p = q.front();q.pop();
        x = p.first;
        y = p.second;
        t = check[x][y];
        for(i = 0; i < 8; i++){
            nx = x+kx[i];
            ny = y+ky[i];
            if(0<=nx && nx<n && 0<=ny && ny<n && D[nx][ny]=='1'){
                nt = max(water_check[nx][ny],t);
                if(check[nx][ny]==-1 || (check[nx][ny]!=-1 && check[nx][ny]>nt)){
                    check[nx][ny]=nt;
                    q.push(make_pair(nx,ny));
                }
            }
        }
    }
    int day = 987654321;
    if (check[n-1][n-2]!=-1) day=min(day,check[n-1][n-2]);
    if (check[n-2][n-2]!=-1) day=min(day,check[n-2][n-2]);
    if (check[n-2][n-1]!=-1) day=min(day,check[n-2][n-1]);
    if(day==INF) cout << -1;
    else cout << day;
}