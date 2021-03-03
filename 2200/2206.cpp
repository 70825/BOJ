#include <bits/stdc++.h>
using namespace std;

int N, M;
int D[1001][1001];
int check[1000][1000][2];
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};
int nx,ny;

struct QQ{
    int x, y, z;
};
queue<QQ> q;

int main(){
    cin >> N >> M;
    memset(D,0,sizeof(D));
    memset(check,-1,sizeof(check));
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++) {
            scanf("%1d", &D[i][j]);
        }
    }
    check[0][0][0]=1;
    q.push({0,0,0});
    while (!q.empty()){
        int x = q.front().x;
        int y = q.front().y;
        int z = q.front().z;
        q.pop();
        for(int i = 0; i<4; i++){
            nx = x+dx[i];
            ny = y+dy[i];
            if (0<=nx && nx<N && 0<=ny && ny<M){
                if (D[nx][ny]==0 && check[nx][ny][z]==-1) {
                    check[nx][ny][z] = check[x][y][z] + 1;
                    q.push({nx, ny, z});
                }
                else if (D[nx][ny]==1 && z==0 && check[nx][ny][1]==-1){
                    check[nx][ny][1]=check[x][y][z] + 1;
                    q.push({nx,ny,1});
                }
            }
        }
    }
    if(check[N-1][M-1][0]==-1)
        cout << check[N-1][M-1][1];
    else if(check[N-1][M-1][1]==-1)
        cout << check[N-1][M-1][0];
    else
        cout << min(check[N-1][M-1][0],check[N-1][M-1][1]);
}