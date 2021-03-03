#include <bits/stdc++.h>
using namespace std;
#define MAX 101

int main()  {
    int n,m,j,x,ans=0;
    cin >> n >> m;
    int now_l = 1, now_r = m;
    cin >> j;

    for(int i=0; i<j; i++){
        cin >> x;
        if(x < now_l){
            ans += now_l - x;
            now_r -= now_l - x;
            now_l = x;
        }
        else if(x > now_r){
            ans += x - now_r;
            now_l += x-now_r;
            now_r = x;
        }
    }
    cout << ans;
}