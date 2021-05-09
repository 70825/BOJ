#include <iostream>
using namespace std;
const int N = 31;

int main()
{
	int n,m,t;
	
	cin >> t;
	while (t--)
	{
		cin >> n >> m;

		long long dp[N][N] = { 0, };
		for (int i = 1; i < N; i++) {
			dp[i][i] = 1;
			dp[1][i] = i;
		}
		for (int i = 2; i < N; i++) {
			for (int j = i + 1; j < N; j++) {
				dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1];
			}
		}

		cout << dp[n][m] << endl;
	}
}