#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 101, K = 1e5+1;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	ll dp[N][K] = { 0, }, W[N] = { 0, }, V[N] = { 0, };

	int n, k;
	cin >> n >> k;

	for (int i = 1; i <= n; i++) cin >> W[i] >> V[i];
	
	ll ans = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j <= k; j++) {
			dp[i][j] = max(dp[i][j], dp[i - 1][j]);
			if (j - W[i] >= 0) dp[i][j] = max(dp[i][j], dp[i - 1][j - W[i]] + V[i]);
			ans = max(ans, dp[i][j]);
		}
	}

	cout << ans;
}