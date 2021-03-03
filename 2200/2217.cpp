#include <bits/stdc++.h>
using namespace std;

int n,ans=0;

int main(){
    cin >> n;
    int D[n];
    for (int i=0; i<n;i++){
        cin >> D[i];
    }
    sort(D,D+n,greater<int>());
    for (int i = 0; i < n; i++){
        ans=max(ans,D[i]*(i+1));
    }
    cout << ans << endl;
}