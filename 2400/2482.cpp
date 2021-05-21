#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1001;
ll MOD = 1e9 + 3;

int n, k;
ll dp[N][N] = { 0, };


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n >> k;

	dp[1][1] = 1;
	for (int i = 2; i <= n; i++) {
		dp[i][0] = dp[i - 1][0];
		dp[i][1] = i;
		for (int j = 2; j <= i / 2; j++) {
			dp[i][j] = (dp[i - 1][j] + dp[i - 2][j - 1]) %  MOD;
		}
	}
	cout << dp[n][k];
}