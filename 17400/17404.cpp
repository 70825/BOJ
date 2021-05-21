#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1001;


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	ll arr[N][3] = { 0, }, dp[3][N][3] = { 0, }; // 처음 색, n번째 집, 색깔
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < 3; j++) cin >> arr[i][j];
	}
	for (int i = 0; i < 3; i++)for (int j = 0; j < N; j++)for (int k = 0; k < 3; k++) dp[i][j][k] = 1e9;

	for (int i = 0; i < 3; i++) dp[i][1][i] = arr[1][i];

	for (int x = 0; x < 3; x++) {
		for (int y = 2; y < n; y++) {
			dp[x][y][0] = min(dp[x][y - 1][1], dp[x][y - 1][2]) + arr[y][0];
			dp[x][y][1] = min(dp[x][y - 1][0], dp[x][y - 1][2]) + arr[y][1];
			dp[x][y][2] = min(dp[x][y - 1][0], dp[x][y - 1][1]) + arr[y][2];
		}
	}

	dp[0][n][1] = arr[n][1] + min(dp[0][n - 1][0], dp[0][n - 1][2]);
	dp[0][n][2] = arr[n][2] + min(dp[0][n - 1][0], dp[0][n - 1][1]);
	dp[1][n][0] = arr[n][0] + min(dp[1][n - 1][1], dp[1][n - 1][2]);
	dp[1][n][2] = arr[n][2] + min(dp[1][n - 1][0], dp[1][n - 1][1]);
	dp[2][n][0] = arr[n][0] + min(dp[2][n - 1][1], dp[2][n - 1][2]);
	dp[2][n][1] = arr[n][1] + min(dp[2][n - 1][0], dp[2][n - 1][2]);
	
	ll ans = 1e9;
	for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) ans = min(ans, dp[i][n][j]);
	cout << ans;

}