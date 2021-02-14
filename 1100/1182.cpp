#include <bits/stdc++.h>
using namespace std;

int D[21],n,s, ans=0;

int go(int x, int y, int c){
    if(y==n+1) return 0;
    go(x+D[y],y+1,1);
    go(x,y+1,0);
    if(x==s && c==1) ans+=1;
    return 0;
}

int main() {
    int val=0;

    cin >> n >> s;
    for(int i=0; i<n; i++)
        cin >> D[i];
    go(val, 0,0);
    cout << ans;
    return 0;
}