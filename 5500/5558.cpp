#include <bits/stdc++.h>
using namespace std;

int n,m,k;
char D[1001][1001];
int check[1001][1001];
int K[11][2];
queue<pair<int,int>>q;
pair<int,int>p;
int ans,nx,ny;
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

int BFS(int sx, int sy, int ex, int ey){
    memset(check,-1,sizeof(check));
    q.push(make_pair(sx,sy));
    check[sx][sy]=0;
    while (!q.empty()){
        p = q.front();q.pop();
        int x = p.first;
        int y = p.second;
        for(int i = 0; i<4; i++){
            nx = x+dx[i];
            ny = y+dy[i];
            if (0<=nx && nx<n && 0<=ny && ny<m && D[nx][ny]!='X' && check[nx][ny]==-1){
                check[nx][ny]=check[x][y]+1;
                q.push(make_pair(nx,ny));
            }
        }
    }
    return check[ex][ey];
}

int main(){
    cin >> n >> m >> k;
    ans=0;
    for(int i = 0; i < n; i++){
        scanf("%s",&D[i]);
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j< m; j++){
            if (D[i][j]=='S') {K[0][0]=i;K[0][1]=j;}
            if(49<=int(D[i][j]) && int(D[i][j])<58){
                K[int(D[i][j])-48][0]=i;
                K[int(D[i][j])-48][1]=j;
            }
        }
    }
    for (int i = 0; i < k; i++)
        ans += BFS(K[i][0],K[i][1],K[i+1][0],K[i+1][1]);
    cout << ans << endl;
}