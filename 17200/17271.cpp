#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 10001, MOD = 1e9+7;
int dp[N], n, m;

int go(int x) {
	if (x == 0) return 1;

	int& ret = dp[x];
	if (ret != -1) return ret;

	ret = 0;
	ret = (ret + go(x - 1)) % MOD;
	if (x - m >= 0) ret = (ret + go(x - m)) % MOD;

	return ret;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n >> m;

	cout << go(n) << endl;
}