#include <iostream>
using namespace std;
typedef long long ll;
const int N = 101;
const int M = 1001;

int main()
{
	int n, s, m;
	cin >> n >> s >> m;

	ll dp[N][M] = { 0, };
	dp[0][s] = 1;
	for (int i = 1; i <= n; i++) {
		int x;
		cin >> x;
		for (int j = 0; j <= m; j++) {
			if (dp[i - 1][j] && j + x <= m) dp[i][j + x] = 1;
			if (dp[i - 1][j] && j - x >= 0) dp[i][j - x] = 1;
		}
	}

	int ans = -1;
	for (int i = 0; i < M; i++) {
		if (dp[n][i]) ans = max(ans, i);
	}
	cout << ans;
}