#include <bits/stdc++.h>
using namespace std;

int main()  {
    int t;
    cin >> t;
    while(t--){
        int x, ans=0;
        int arr[4];
        cin >> x;
        while(true){
            if(x == 6174) break;
            for(int i=0; i<4; i++){
                arr[i] = x % 10;
                x /= 10;
            }
            int a=0,b=0;
            sort(arr,arr+4);
            for(int i=0; i<4; i++){
                a = a * 10 + arr[i];
                b = b * 10 + arr[3-i];
            }
            x = b - a;
            ans += 1;
        }
        cout << ans << endl;
    }
}