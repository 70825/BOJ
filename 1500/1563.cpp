#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1001;
int MOD = 1e6;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	ll dp[N][2][3] = { 0, };
	dp[0][0][0] = 1;
	for (int i = 1; i <= n; i++) {
		dp[i][0][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % MOD;

		dp[i][1][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % MOD;
		dp[i][1][0] += (dp[i - 1][1][0] + dp[i - 1][1][1] + dp[i - 1][1][2]) % MOD;

		for (int j = 0; j < 2; j++) for (int k = 1; k < 3; k++) dp[i][j][k] = dp[i - 1][j][k - 1];
	}
	ll ans = 0;
	for (int i = 0; i < 2; i++) for (int j = 0; j < 3; j++) ans = (ans + dp[n][i][j]) % MOD;
	cout << ans;

}