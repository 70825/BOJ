#include <bits/stdc++.h>
using namespace std;

queue<pair<int,int>>q;
pair<int,int> p;

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

char D[101][101];
int S[101][101];

int n,m,nx,ny,x,y;

int main()
{
    memset(D,0,sizeof(D));
    memset(S,0,sizeof(S));

    cin >> n >> m;

    for(int i = 0; i<n; i++)
        cin >> D[i];

    S[0][0]=1;
    q.push(make_pair(0,0));

    while(!q.empty())
    {
        p = q.front();q.pop();
        x = p.first;
        y = p.second;

        for(int i = 0; i<4; i++){
            nx = x + dx[i];
            ny = y + dy[i];
            if(0<=nx && nx<n && 0<=ny && ny<m && S[nx][ny] == 0 && D[nx][ny] == '1'){
                S[nx][ny] = S[x][y] + 1;
                q.push(make_pair(nx,ny));
            }
        }
    }

    cout << S[n-1][m-1] << endl;
    return 0;
}