#include <iostream>
#include <cstring>
#include <string>
using namespace std;
using ll = long long;

int t, n, k;
ll dp[1 << 15][100], ten[51], mod[15];
string str[15];

ll gcd(ll x, ll y) {
	ll tmp;
	while (y != 0) {
		tmp = x % y;
		x = y;
		y = tmp;
	}

	return x;
}

int modular(string x) {
	int val = 0;
	for (int i = 0; i < x.size(); i++) {
		val = (val * 10 + (x[i] - '0')) % k;
	}
	return val;
}

ll go(int visit, int val) {
	if (visit == (1 << n) - 1) return val == 0 ? 1 : 0;

	ll& ret = dp[visit][val];
	if (ret != -1) return ret;

	ret = 0;
	for (int i = 0; i < n; i++) {
		if ((visit & (1 << i)) == 0) {
			ret += go(visit | (1 << i), (val * ten[str[i].size()] + mod[i]) % k);
		}
	}

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	memset(dp, -1, sizeof(dp));

	cin >> n;
	for (int i = 0; i < n; i++) cin >> str[i];
	cin >> k;

	for (int i = 0; i < n; i++) mod[i] = modular(str[i]);

	ten[0] = 1;
	for (int i = 1; i < 51; i++) {
		ten[i] = (ten[i - 1] * 10) % k;
	}



	ll ans = 0;
	for (int i = 0; i < n; i++) {
		ans += go(1 << i, mod[i]);
	}

	ll fac = 1;
	for (int i = 1; i <= n; i++) {
		fac *= i;
	}

	if (ans == 0) cout << "0/1";
	else if (ans == fac) cout << "1/1";
	else cout << ans / gcd(fac, ans) << "/" << fac / gcd(fac, ans);

	cout << endl;
}