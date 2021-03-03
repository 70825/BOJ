#include <bits/stdc++.h>
using namespace std;

int co[1000] = {0};

void find(int x,int y, int z){
    int A[4],B[4];

    for(int i=0; i<3; i++){
        A[2-i] = x%10;
        x/=10;
    }

    for(int i=111; i<1000; i++){
        int k = i, ball = 0, strike = 0, num[10] = {0};
        for(int j=0; j<3; j++){
            B[2-j] = k%10;
            num[k%10]=1;
            k/=10;
        }
        for(int j=0; j<3; j++){
            if(A[j]==B[j]) strike+=1;
            else
                if(num[A[j]]!=0) ball+=1;
        }
        if(strike!=y || ball!=z) co[i]=0;
    }
}

int main() {
    int n,x,y,z,ans=0;

    cin >> n;

    for(int i=1; i<10; i++)
        for(int j=1; j<10; j++)
            for(int k=1; k<10; k++)
                if(i!=j && j!=k && k!=i) co[100*i+10*j+k]=1;

    for(int i=0; i<n; i++){
        cin >> x >> y >> z;
        find(x,y,z);
    }
    for(int i=111; i<1000; i++)
        ans+=co[i];

    cout << ans;
}