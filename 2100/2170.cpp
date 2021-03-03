#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n,res=0,right,left;
    cin >> n;
    pair<int,int> D[n];
    for(int i=0; i<n; i++){
        cin >> D[i].first >> D[i].second;
    }
    sort(D,D+n);
    left=D[0].first;
    right=D[0].second;
    for(int i=1; i<n; i++){
        if(right<D[i].first){
            res+=right-left;
            left=D[i].first;
            right=D[i].second;
        }
        else right=max(right,D[i].second);
    }
    res+=right-left;
    cout << res << "\n";
}