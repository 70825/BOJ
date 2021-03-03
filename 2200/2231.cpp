#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;

    cin >> n;

    for(int i=0; i<n; i++)
    {
        int ans=i, k=i;
        while(k!=0)
        {
            ans += k%10;
            k /= 10;
        }
        if(ans==n)
        {
            cout << i;
            return 0;
        }
    }
    cout << 0;
    return 0;
}
