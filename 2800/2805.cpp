#include <bits/stdc++.h>
using namespace std;

int n, m, A[1000001];
int low = 0, high = 1000000000, mid;
long long val;

int main()
{

    cin >> n >> m;

    for(int i=0; i<n; i++)
        cin >> A[i];

    while (low + 1 < high)
    {
        mid = (low + high) / 2;

        val = 0;
        for(int i = 0; i < n; i++)
            if(A[i] - mid > 0)
                val += A[i] - mid;
        if(val >= m) low = mid;
        else high = mid;
    }

    cout << low;

    return 0;
}