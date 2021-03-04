#include <bits/stdc++.h>
using namespace std;

int N, K;
int D[100001];
int C[100001];
queue<int> q;
int dx[3] = {1, -1, 0};

int main(){
    cin >> N >> K;
    q.push(N);
    memset(D,-1,sizeof(D));
    memset(C,0,sizeof(C));
    D[N]=0;C[N]=1;
    while(!q.empty()){
        int x = q.front();q.pop();
        dx[2]= x;
        for(int i = 0; i < 3; i++) {
            int nx = x + dx[i];
            if (0 <= nx && nx <= 100000) {
                if (D[nx]==-1){
                    D[nx] = D[x]+1;
                    C[nx]=C[x];
                    q.push(nx);
                }
                else if (D[nx]==D[x]+1){
                    C[nx]+=C[x];
                }
            }
        }
    }
    cout << D[K] << endl;
    cout << C[K] << endl;
    return 0;
}