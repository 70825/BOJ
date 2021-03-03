#include <bits/stdc++.h>
using namespace std;

int n,k;
int D[10000]={0,};

int main(){
    cin >> n;
    cin >> k;
    for(int i = 0; i < n; i++){
        cin >> D[i];
    }
    sort(D,D+n,less<int>());
    vector<int> S(D,D+n);
    S.erase(unique(S.begin(),S.end()),S.end());
    vector<int> K;
    for(int i = 1; i < S.size(); i++){
        K.push_back(S[i]-S[i-1]);
    }
    sort(K.begin(),K.end(),greater<int>());
    int ans = 0;
    if (k>=K.size()) cout << 0 << endl;
    else{
        for(int i = 0; i < K.size(); i++){ans+=K[i];}
        for(int i = 0; i < k-1; i++){ans-=K[i];}
        cout << ans << endl;
    }
}