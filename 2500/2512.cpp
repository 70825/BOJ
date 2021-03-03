#include <bits/stdc++.h>
using namespace std;

int n,m;
int D[10000]={0,};

int main(){
    cin >> n;
    int Min = 0, Max = 0;
    for(int i = 0; i < n; i++){
        cin >> D[i];
        if (D[i]>Max) Max=D[i];
    }
    cin >> m;
    while(Min<=Max){
        int mid = (Min+Max)/2;
        long long ans = 0;
        for(int i = 0; i<n; i++){
            ans+=min(mid,D[i]);
        }
        if(ans<=m) Min=mid+1;
        else Max=mid-1;
    }
    cout << (Min+Max)/2 << endl;
}