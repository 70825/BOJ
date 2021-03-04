#include <bits/stdc++.h>
using namespace std;

int n,m;
int D[100000]={0,};
long long k = 100000*10001;

int main(){
    cin >> n >> m;
    int Min = 0, Max = 0;
    for(int i = 0; i < n; i++){
        cin >> D[i];
        Max+=D[i];
    }
    while(Min<=Max){
        int mid = (Min+Max)/2;
        long long ans = 0, z = 0, s = 0;
        for(int i = 0; i<n; i++){
            if(ans+D[i]<=mid) ans+=D[i];
            else{
                z=max(z,ans);
                ans=D[i];
                s+=1;
            }
        }
        s+=1;
        if(s<=m){
            k=min(k,max(z,ans));
            Max=mid-1;
        }
        else Min=mid+1;
    }
    cout << k << endl;
}