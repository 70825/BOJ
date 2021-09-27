#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 101, M = 1001, P = 501, MIN = -987654321;
int n, m, k, dp[M][P], cp[N], mem[N], pri[N];

int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n >> m >> k;
	for (int i = 0; i < n; i++) {
		cin >> cp[i] >> mem[i] >> pri[i];
	}

	for (int i = 0; i < n; i++) {
		for (int j = m; j >= 1; j--) {
			for (int p = P-1; p >= 1; p--) {
				if (dp[j][p] == -1) continue;
				dp[min(j + cp[i], m)][p + pri[i]] = max(dp[min(j + cp[i], m)][p + pri[i]], dp[j][p] + mem[i]);
			}
		}
		dp[cp[i]][pri[i]] = max(dp[cp[i]][pri[i]], mem[i]);
	}

	int ans = -1;
	for (int i = 0; i < P; i++) {
		if (dp[m][i] >= k) {
			ans = i;
			break;
		}
	}
	cout << ans << endl;

	return 0;
}