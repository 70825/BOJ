#include <bits/stdc++.h>
using namespace std;

int n,m,A[500001],B[500001];
int low, high, mid, res;

int main()
{
    scanf("%d",&n);
    for(int i=0; i<n; i++)
        scanf("%d",&A[i]);
    scanf("%d",&m);
    for(int i=0; i<m; i++)
        scanf("%d",&B[i]);

    sort(A,A+n);

    for(int i = 0; i < m; i++)
    {
        low = 0;
        high = n-1;
        res = 0;

        while (low <= high)
        {
            mid = (low + high) / 2;
            if (B[i] == A[mid])
            {
                res = 1;
                break;
            }
            if (A[mid] > B[i]) high = mid - 1;
            else low = mid + 1;
        }

        cout << res << " ";
    }

    return 0;
}