#include <bits/stdc++.h>
using namespace std;

int main()  {
    int n;
    char D[50][5][7];
    cin >> n;
    for(int i=0; i<n; i++) for(int j=0; j<5; j++) for(int k=0; k<7; k++) cin >> D[i][j][k];
    int ans[3] = {0, -1, -1};
    for(int i=0; i<n; i++)
        for(int j=i+1; j<n; j++){
            int z = 0;
            for(int x=0; x<5; x++)for(int y=0; y<7; y++)if(D[i][x][y] == D[j][x][y]) z += 1;
            if(z > ans[0]){
                ans[0] = z;
                ans[1] = i;
                ans[2] = j;
            }
        }
    cout << ans[1] + 1 << " " << ans[2] + 1 << endl;
}