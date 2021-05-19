#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 31;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	ll dp[N][N] = { 0, };
	for (int i = 1; i < N; i++) dp[i][0] = 1;
	for (int i = 1; i < N; i++) {
		for (int j = 1; j <= i; j++) {
			dp[i][j] += dp[i - 1][j] + dp[i][j - 1];
		}
	}

	int n;
	while (1) {
		cin >> n;
		if (!n) break;

		cout << dp[n][n]<<endl;
	}
	
}