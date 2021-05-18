#include <iostream>
using namespace std;
typedef long long ll;
const int N = 16;

int main()
{
	int n, m, k;
	cin >> n >> m >> k;
	k = max(0, k - 1);

	int x = k / m, y = k % m;

	ll dp[N][N] = { 0, };
	for (int i = 0; i <= x; i++) {
		for (int j = 0; j <= y; j++) {
			if (!i || !j) dp[i][j] = 1;
			else dp[i][j] = dp[i - 1][j] + dp[i][j-1];
		}
	}
	for (int i = x; i < n; i++) {
		for (int j = y; j < m; j++) {
			if (i == x || j == y) dp[i][j] = dp[x][y];
			else dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
		}
	}
	cout << dp[n - 1][m - 1];
}