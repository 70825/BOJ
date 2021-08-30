#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 1e4 + 1, MOD = 1e9 + 7;
int t, n;
ll dp[N][2][7];

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	memset(dp, 0, sizeof(dp));
	dp[1][1][0] = 1;
	for (int i = 1; i < 10; i++) {
		if (i != 7) dp[1][0][i % 7]++;
	}

	for (int i = 1; i < N - 1; i++) {
		for (int j = 0; j < 2; j++) {
			for (int k = 0; k < 7; k++) {
				for (int l = 0; l < 10; l++) {
					if (l == 0 || l == 7) dp[i + 1][1][k] = (dp[i + 1][1][k] + dp[i][j][k]) % MOD;
					else dp[i + 1][j][(k + l) % 7] = (dp[i + 1][j][(k + l) % 7] + dp[i][j][k]) % MOD;
				}}}}

	cin >> t;
	while (t--) {
		cin >> n;
		cout << dp[n][1][0] << '\n';
	}
}