#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

int t, n;
int dp[30][13];

int go(int x, int bit) {
	if (x == 1 && bit == 6) return 0;
	if (x == 1 || x == 0) return 1;

	int& ret = dp[x][bit];
	if (ret != -1) return ret;

	ret = 0;
	if (bit == 0) ret += go(x - 1, 0) + go(x - 2, 0) + go(x - 1, 3) + go(x - 1, 9) + go(x - 1, 12);
	else if (bit == 3) ret += go(x - 1, 0) + go(x - 1, 12);
	else if (bit == 6) ret += go(x - 1, 9);
	else if (bit == 9) ret += go(x - 1, 0) + go(x - 1, 6);
	else ret += go(x - 1, 0) + go(x - 1, 3);

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	memset(dp, -1, sizeof(dp));

	cin >> t;
	while (t--) {
		cin >> n;
		cout << go(n, 0) << endl;
	}

	return 0;
}