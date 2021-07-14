#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 101;
int n, l, r, MOD = 1e9 + 7;
ll dp[N][N][N];

ll go(int x, int L, int R) {
	if (!x || !L || !R) return 0;
	ll& ret = dp[x][L][R];
	if (ret != -1) return ret;

	ret = (go(x - 1, L - 1, R) + go(x - 1, L, R - 1) + go(x - 1, L, R) * (x - 2)) % MOD;
	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));
	
	cin >> n >> l >> r;

	dp[1][1][1] = 1;
	cout << go(n, l, r) << endl;
}