#include <bits/stdc++.h>
using namespace std;
#define MAX 1000000

int main()  {
    int n,b,c;
    long long ans=0;
    int A[MAX];

    cin >> n;
    for(int i=0; i<n; i++) cin >> A[i];
    cin >> b >> c;

    for(int i=0; i<n; i++){
        ans += 1;
        A[i]-=b;
        if(A[i]>0){
            if(A[i]%c == 0) ans += A[i]/c;
            else ans += A[i]/c + 1;
        }
    }
    cout << ans;
}