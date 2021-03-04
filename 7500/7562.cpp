#include <bits/stdc++.h>
using namespace std;

queue<pair<int,int>>q;
pair<int,int>p;

int dx[8] = {2,2,1,1,-1,-1,-2,-2};
int dy[8] = {-1,1,-2,2,2,-2,-1,1};

int S[301][301];

int t,l,x,y,sx,sy,ex,ey,nx,ny;

int main()
{
    cin >> t;

    for(int i = 0; i<t;i++)
    {
        memset(S,-1,sizeof(S));

        cin >> l;
        cin >> sx >> sy;
        cin >> ex >> ey;

        S[sx][sy] = 0;
        q.push(make_pair(sx,sy));

        while(!q.empty())
        {
            p = q.front(); q.pop();
            x = p.first;
            y = p.second;
            for(int j=0; j<8;j++)
            {
                nx = x+dx[j];
                ny = y+dy[j];
                if(0<=nx && nx<l && 0<=ny && ny<l && S[nx][ny]==-1)
                {
                    S[nx][ny] = S[x][y]+1;
                    q.push(make_pair(nx,ny));
                }
            }
        }

        cout << S[ex][ey] << endl;
    }

    return 0;
}