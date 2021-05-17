#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1001;

int main()
{
	int t,w;
	cin >> t >> w;

	ll time[N] = { 0, };
	for (int i = 1; i <= t; i++) cin >> time[i];

	ll dp[2][N][31] = { 0, };
	if (time[1] == 1) {
		dp[0][1][0] = 1;
		dp[0][1][1] = 1;
	}
	else dp[1][1][1] = 1;

	for (int i = 2; i <= t; i++) {
		for (int j = 0; j <= min(i,w); j++) {
			dp[0][i][j] = dp[0][i - 1][j];
			dp[1][i][j] = dp[1][i - 1][j];
			if (j > 0) {
				dp[0][i][j] = max(dp[0][i][j], dp[1][i - 1][j - 1]);
				dp[1][i][j] = max(dp[1][i][j], dp[0][i - 1][j - 1]);
			}
			dp[time[i] - 1][i][j]++;
		}
	}

	ll ans = 0;
	for (int i = 0; i <= w; i++)ans = max(ans, max(dp[0][t][i], dp[1][t][i]));

	cout << ans;
}