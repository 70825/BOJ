#include <bits/stdc++.h>
using namespace std;
#define SWAP(x,y) (x=x^y,y=x^y,x=x^y)
#define MAX(x,y) (x>y? x:y)

int n, Max=1;
char candy[51][51];

int find(){
    int x=1, max=1;

    for(int i=0; i<n; i++) {
        char B = candy[i][0]; x=1;
        for (int j = 1; j < n; j++) {
            if (candy[i][j] != B) {
                max = MAX(x, max);
                B = candy[i][j];
                x = 1;
            } else x += 1;
            max = MAX(x,max);
        }
    }
    for(int i=0;i<n;i++){
        char B = candy[0][i]; x=1;
        for(int j=1;j<n;j++){
            if(candy[j][i] != B){
                max = MAX(x,max);
                B = candy[j][i];
                x=1;
            }
            else x+=1;
            max = MAX(x,max);
        }

    }

    return max;
}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> candy[i][j];
    for(int i = 0; i<n; i++)
        for(int j=0; j<n-1;j++)
        {
            SWAP(candy[i][j],candy[i][j+1]);
            Max = MAX(find(),Max);
            SWAP(candy[i][j],candy[i][j+1]);
            SWAP(candy[j][i],candy[j+1][i]);
            Max = MAX(find(),Max);
            SWAP(candy[j][i],candy[j+1][i]);
        }
    cout << Max;

    return 0;
}