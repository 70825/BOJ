#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;

const int N = 1e5 + 1;

int dp[N][5][5], val[N];

int go(int x, int l, int r) {
	if (val[x] == 0) return 0;

	int& ret = dp[x][l][r];
	if (ret != -1) return ret;

	ret = 5 * N;
	int y = val[x];

	if (l == y || r == y) ret = min(ret, go(x + 1, l, r) + 1);

	if (l == 0) ret = min(ret, go(x + 1, y, r) + 2);
	if (r != y) {
		if ((4 + y - l) % 2) ret = min(ret, go(x + 1, y, r) + 3);
		else ret = min(ret, go(x + 1, y, r) + 4);
	}

	if (r == 0) ret = min(ret, go(x + 1, l, y) + 2);
	if (l != y) {
		if ((4 + y - r) % 2) ret = min(ret, go(x + 1, l, y) + 3);
		else ret = min(ret, go(x + 1, l, y) + 4);
	}

	return ret;
}


int main() {
	memset(dp, -1, sizeof(dp));

	for (int i = 0; i < N; i++) {
		cin >> val[i];
		if (!val[i]) break;
	}

	if (val[0] == 0) {
		cout << 0 << endl;
		return 0;
	}

	go(0, 0, 0);

	cout << dp[0][0][0] << endl;

	return 0;
}