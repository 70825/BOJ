#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 1000002, M = 102;
int n, m, W[M], V[M], bag[M], dp[M][N];

ll gcd(int a, int b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

ll lcm(int a, int b) {
	return a * (b / gcd(a, b));
}

int main() {
	cin.tie(0); cout.tie(0);
	memset(dp, 0, sizeof(dp));

	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		cin >> W[i] >> V[i];
	}
	for (int i = 1; i <= m; i++) {
		cin >> bag[i];
	}

	for (int i = 1; i <= n; i++) { 
		for (int j = 0; j < N - 1; j++) {
			dp[i][j] = max(dp[i][j], dp[i - 1][j]);
			if (j - W[i] >= 0) dp[i][j] = max(dp[i][j], dp[i - 1][j - W[i]] + V[i]);
		}
	}

	int ans = 1;

	for (int i = 2; i <= m; i++) {
		ll LCM = lcm(bag[ans], bag[i]);
		ll val1 = dp[n][bag[ans]] * (LCM / bag[ans]);
		ll val2 = dp[n][bag[i]] * (LCM / bag[i]);

		if (val2 > val1) ans = i;
	}

	cout << ans << endl;

	return 0;
}