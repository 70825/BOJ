#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1e6+1;
const int MOD = 9901;

int main()
{
	int n;
	cin >> n;

	ll dp[N][3] = { 0, };
	for (int i = 0; i < 3; i++) dp[0][i]++;

	for (int i = 1; i < n; i++) {
		dp[i][0] += (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2])%MOD;
		dp[i][1] += (dp[i - 1][0] + dp[i - 1][2])%MOD;
		dp[i][2] += (dp[i - 1][0] + dp[i - 1][1])%MOD;
	}

	cout << (dp[n - 1][0] + dp[n - 1][1] + dp[n - 1][2]) % MOD;


}