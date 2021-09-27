#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 101, M = 1001, P = 501, MIN = -987654321;
int n, m, k, dp[N][M][P], cp[N], mem[N], pri[N];

int go(int x, int cpu_, int p) {
	if (x == n) return cpu_ >= m ? 0 : MIN;

	int& ret = dp[x][cpu_][p];
	if (ret != -1) return ret;

	int ncpu = min(cpu_ + cp[x], 1000);
	ret = max(go(x + 1, cpu_, p), p - pri[x] >= 0 ? go(x + 1, ncpu, p - pri[x]) + mem[x] : MIN);

	return ret;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n >> m >> k;
	for (int i = 0; i < n; i++) {
		cin >> cp[i] >> mem[i] >> pri[i];
	}

	for (int i = 0; i < P; i++) {
		int x = go(0, 0, i);
		if (x >= k) {
			cout << i << endl;
			return 0;
		}
	}
	cout << -1 << endl;

	return 0;
}