#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,m,max=2e9;
    string chess_board[51];

    cin >> n >> m;

    for(int i=0; i<n; i++)
        cin >> chess_board[i];

    for(int i=0; i<n-7; i++)
        for(int j=0; j<m-7; j++) {
            int W1=0,B1=0,W2=0,B2=0;
            for (int x = i; x < i + 8; x++)
                for (int y = j; y < j + 8; y++){
                    if(x%2==i%2){
                        if(y%2==j%2) chess_board[x][y]=='W'? W2+=1:B1+=1;
                        else chess_board[x][y]=='B'? B2+=1:W1+=1;
                    }
                    else{
                        if(y%2==j%2) chess_board[x][y]=='B'? B2+=1:W1+=1;
                        else chess_board[x][y]=='W'? W2+=1:B1+=1;
                    }
                }
            max = min({max,W1+B1,W2+B2});
        }
    cout << max;
    return 0;
}