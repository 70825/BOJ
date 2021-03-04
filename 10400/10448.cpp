#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x[45], num[1001]={0};

    cin >> n;

    for(int i=1; i<45; i++)
        x[i-1] = i*(i+1)/2;

    for(int i=0; i<44; i++)
        for(int j=i; j<44; j++)
            for(int k=j; k<44; k++){
                int ans = x[i]+x[j]+x[k];
                if(ans<=1000) num[ans]=1;
            }


    for(int i=0; i<n; i++){
        int y;
        cin >> y;
        if(num[y]==1) cout << 1 << endl;
        else cout << 0 << endl;
    }

    return 0;
}