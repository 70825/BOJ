#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 101, MOD = 1e9;
int n;
ll dp[10][N][1 << 10];

ll go(int x, int y, int visit) {
	if (y == n) {
		if (visit == (1 << 10) - 1) return 1;
		else return 0;
	}
	ll& ret = dp[x][y][visit];
	if (ret != -1) return ret;

	ret = 0;
	if (x == 0) ret = go(1, y + 1, visit | 1 << 1);
	else if (x == 9) ret = go(8, y + 1, visit | 1 << 8);
	else {
		ret = (ret + go(x - 1, y + 1, visit | 1 << (x - 1)) + go(x + 1, y + 1, visit | 1 << (x + 1))) % MOD;
	}

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));


	cin >> n;

	ll ans = 0;

	for (int i = 1; i < 10; i++) ans = (ans + go(i, 1, 1 << i)) % MOD;

	cout << ans;

	return 0;
}