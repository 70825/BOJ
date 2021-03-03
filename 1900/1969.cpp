#include <bits/stdc++.h>
using namespace std;

int n,m;

int main(){
    cin >> n >> m;
    int D[m][4];
    memset(D,0,sizeof(D));
    string k;
    for (int i=0; i<n;i++){
        cin >> k;
        for (int j=0; j<m; j++){
            if(k[j]=='A') D[j][0]+=1;
            else if(k[j]=='C') D[j][1]+=1;
            else if(k[j]=='G') D[j][2]+=1;
            else D[j][3]+=1;
        }
    }
    int ans = 0;
    for (int i = 0; i<m; i++){
        int Max=0;
        for(int j = 0; j<4; j++){
            if(D[i][Max]<D[i][j]) Max=j;
        }
        if(Max==0) cout << 'A';
        else if(Max==1) cout << 'C';
        else if(Max==2) cout << 'G';
        else cout << 'T';
        ans+=D[i][0]+D[i][1]+D[i][2]+D[i][3]-D[i][Max];
    }
    cout << endl;
    cout << ans << endl;
}