#include <bits/stdc++.h>
using namespace std;

char D[501];

int main(){
    memset(D,'z',sizeof(D));
    scanf("%s",&D);
    int leng = 0;
    for (int i = 0; i < 501; i++){
        if (D[i]=='z'){
            leng = i;
            break;
        }
    }
    int i = 0;
    while(i < leng-1){
        if (i+3 < leng-1 && D[i]=='X' && D[i+1]=='X' && D[i+2]=='X' && D[i+3]=='X'){
            D[i]='A';D[i+1]='A';D[i+2]='A';D[i+3]='A';
            i+=4;
        }
        else if (i+1 < leng-1 && D[i]=='X' && D[i+1]=='X'){
            D[i]='B';D[i+1]='B';
            i+=2;
        }
        else if (D[i]=='.'){i+=1;}
        else{
            cout << -1 <<endl;
            return 0;
        }
    }
    cout << D << endl;
}