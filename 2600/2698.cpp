#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 101;

int n, k;
ll dp[N][N][2] = { 0, };

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	dp[1][0][0] = 1;
	dp[1][0][1] = 1;
	for (int i = 2; i < N; i++) {
		dp[i][0][0] = dp[i - 1][0][0] + dp[i - 1][0][1];
		dp[i][0][1] = dp[i - 1][0][0];
		for (int j = 1; j < i; j++) {
			dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1];
			dp[i][j][1] = dp[i - 1][j - 1][1] + dp[i - 1][j][0];
		}
	}

	int t;
	cin >> t;
	while (t--) {
		cin >> n >> k;
		cout << dp[n][k][0] + dp[n][k][1] << endl;
	}

}