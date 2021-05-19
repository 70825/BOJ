#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 2001;
int n;
int A[N] = { 0, }, B[N] = { 0, }, dp[N][N] = { 0, };

int go(int x, int y) {
	if (x == n || y == n) return 0;
	if (dp[x][y] != -1) return dp[x][y];

	int res = 0;
	if (A[x] > B[y]) res += B[y] + go(x, y + 1);
	else res += max(go(x + 1, y), go(x + 1, y + 1));
	dp[x][y] = res;

	return res;
}

int main()
{
	cin >> n;

	memset(dp, -1, sizeof(dp));
	for (int i = 0; i < n; i++) cin >> A[i];
	for (int i = 0; i < n; i++) cin >> B[i];

	cout << go(0, 0);
}