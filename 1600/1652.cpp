#include <bits/stdc++.h>
using namespace std;
#define MAX 101

int main()  {
    int n, ans1 = 0, ans2 = 0;
    char D[MAX][MAX];
    int garo[MAX][MAX]={0}, sero[MAX][MAX] = {0};

    cin >> n;
    for(int i=0; i<n; i++) for(int j=0; j<n; j++) cin >> D[i][j];
    for(int i=0; i<n; i++){
        if(D[i][0] == '.') garo[i][0] = 1;
        for(int j=1; j<n; j++) {
            if (D[i][j] == '.') garo[i][j] = garo[i][j - 1] + 1;
            if (D[i][j] == 'X' && garo[i][j - 1] >= 2) ans1 += 1;
        }
        if(D[i][n-1] == '.' && garo[i][n-1] >= 2) ans1 += 1;
    }
    for(int j=0; j<n; j++){
        if(D[0][j] == '.') sero[0][j] = 1;
        for(int i=1; i<n; i++){
            if(D[i][j] == '.') sero[i][j] = sero[i-1][j] + 1;
            if(D[i][j] == 'X' && sero[i-1][j] >= 2) ans2 += 1;
        }
        if(D[n-1][j] == '.' && sero[n-1][j] >= 2) ans2 += 1;
    }
    cout << ans1 << " " << ans2 << endl;
}