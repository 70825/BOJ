#include <iostream>
#include <string>
using namespace std;
typedef long long ll;
const int N = 1001;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n, m;
	cin >> n >> m;

	int arr[N][N] = { 0, }, dp[N][N] = { 0, };

	string x;
	for (int i = 1; i <= n; i++) {
		cin >> x;
		for (int j = 0; j < m; j++) {
			arr[i][j+1] = (int)x[j] - '0';
		}
	}

	int ans = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (arr[i][j] == 1) {
				if (dp[i - 1][j - 1] != 0 && dp[i][j - 1] != 0 && dp[i - 1][j] != 0) {
					dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1;
				}
				else dp[i][j] = 1;
				ans = max(ans, dp[i][j]*dp[i][j]);
			}
		}
	}
	cout << ans;
}