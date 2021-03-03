#include <bits/stdc++.h>
using namespace std;

int n,m;
char D[51][51];
queue<pair<int,int>>q;
pair<int,int>p;
int ans,nx,ny;
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

int BFS(int x, int y){
    int z = 0;
    int check[101][101];
    memset(check,-1,sizeof(check));
    q.push(make_pair(x,y));
    check[x][y]=0;
    while (!q.empty()){
        p = q.front();q.pop();
        x = p.first;
        y = p.second;
        for(int i = 0; i<4; i++){
            nx = x+dx[i];
            ny = y+dy[i];
            if (0<=nx && nx<n && 0<=ny && ny<m && D[nx][ny]=='L' && check[nx][ny]==-1){
                z=max(z,check[x][y]+1); check[nx][ny]=check[x][y]+1;q.push(make_pair(nx,ny));
            }
        }
    }
    return z;
}

int main(){
    cin >> n >> m;
    ans=0;
    for(int i = 0; i < n; i++){
        scanf("%s",&D[i]);
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j< m; j++){
            if(D[i][j]=='L') ans=max(ans,BFS(i,j));
        }
    }
    cout << ans << endl;
}