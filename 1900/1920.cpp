#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n,m,A[100001],B[100001];
    int low, high, mid, val, res = 0;

    scanf("%d", &n);
    for(int i = 0; i < n; i++)
        scanf("%d", &A[i]);
    scanf("%d", &m);
    for(int i = 0; i < m; i++)
        scanf("%d", &B[i]);

    sort(A, A+n);

    for(int i = 0; i < m; i++)
    {
        low = 0;
        high = n-1;
        val = B[i];
        res = 0;

        while(low <= high)
        {
            mid = (low + high) / 2;

            if (A[mid] == val)
            {
                res = 1;
                break;
            }
            if (A[mid] > val)
                high = mid - 1;
            if (A[mid] < val)
                low = mid + 1;
        }

        cout << res << "\n";
    }

    return 0;
}