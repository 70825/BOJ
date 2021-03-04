#include<iostream>
using namespace std;

int main() {
    int x, n, y;

    scanf("%d %d", &n, &x);

    for(int i=0; i<n; i++)
    {
        scanf("%d",&y);
        if(y<x) printf("%d ",y);
    }

    return 0;
}
