#include <iostream>
using namespace std;
typedef long long ll;
const int N = 501;
const int M = 1001;

int main()
{
	int n;
	cin >> n;
	
	ll arr[N][N] = { 0, };
	ll dp[N][N] = { 0, };

	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) cin >> arr[i][j];
	}
	dp[0][0] = arr[0][0];
	for (int i = 1; i < n; i++) {
		dp[i][0] = arr[i][0] + dp[i - 1][0];
		dp[i][i] = arr[i][i] + dp[i - 1][i - 1];
		for (int j = 1; j < i; j++) dp[i][j] = arr[i][j] + max(dp[i - 1][j - 1],dp[i - 1][j]);
	}

	ll ans = 0;
	for (int i = 0; i < n; i++) ans = max(ans, dp[n - 1][i]);
	cout << ans;
}