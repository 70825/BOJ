#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 2501;
int MOD = 1e9 + 7;


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	ll dp[N] = { 0, };
	dp[0] = 1;
	for (int i = 1; i < N; i ++) {
		for (int j = 0; j < i; j++) {
			dp[i] = (dp[i] + (dp[j] * dp[i - j - 1]) % MOD) % MOD;
		}
	}

	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		if (n % 2 == 1) cout << 0 << endl;
		else cout << dp[n / 2] << endl;
	}
}