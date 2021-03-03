#include <bits/stdc++.h>
using namespace std;

int n,m,k;
int Land[101];
int D[101][1001];
int check[16384][101];
queue<pair<int,int>> q;
pair<int,int>p;


int main(){
    memset(Land,-1,sizeof(Land));
    memset(D,-1,sizeof(D));
    memset(check,-1,sizeof(check));
    cin >> n >> m >> k;
    int ans = 0;
    for(int i = 0; i < k; i++) {
        int z;
        cin >> z;
        Land[z-1] = i;
    }
    for(int i = 0; i < m; i++){
        int a,b,c;
        cin >> a >> b >> c;
        D[a-1][b-1]=c;
        D[b-1][a-1]=c;
    }
    check[0][0]=0;
    q.push(make_pair(0,0));
    while(!q.empty()){
        p = q.front();q.pop();
        int key = p.first;
        int x = p.second;
        if(x==0) ans=max(check[key][x],ans);
        if(Land[x]!=-1 && !(key & 1<<Land[x])){
            int nkey = key | 1<<Land[x];
            if(check[nkey][x]<check[key][x]+1){
                check[nkey][x]=check[key][x]+1;
                q.push(make_pair(nkey, x));
            }
        }
        for(int i = 0; i < n; i++){
            int nx = i;
            int Max = D[x][i];
            if(check[key][x]<=Max && check[key][nx]<check[key][x]){
                check[key][nx]=check[key][x];
                q.push(make_pair(key,nx));
            }
        }
    }
    cout << ans << endl;
}