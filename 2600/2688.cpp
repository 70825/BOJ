#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 65;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	ll dp[N][10] = { 0, };
	for (int i = 0; i < 10; i++) dp[1][i] = 1;

	for (int i = 2; i < N; i++) {
		for (int j = 0; j < 10; j++) {
			for (int k = 0; k <= j; k++) {
				dp[i][j] += dp[i - 1][k];
			}
		}
	}

	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;

		ll ans = 0;
		for (int i = 0; i < 10; i++) ans += dp[n][i];
		cout << ans << endl;
	}
}