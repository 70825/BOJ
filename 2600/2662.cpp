#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
typedef long long ll;

int n, m;
ll cost[22][302], dp[22][302], path[22][302];

ll go(int x, int left) {
	if (x > m) return 0;
	ll& ret = dp[x][left];
	if (ret != -1) return ret;

	ret = 0;
	for (int i = 0; i <= left; i++) {
		ll z = cost[x][i] + go(x + 1, left - i);
		if (ret < z) {
			ret = z;
			path[x][left] = i;
		}
	}
	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n >> m;

	int x;
	for (int i = 1; i <= n; i++) {
		cin >> x;
		for (int j = 1; j <= m; j++) {
			cin >> cost[j][x];
		}
	}

	
	cout << go(1, n) << endl;

	x = n;
	for (int i = 1; i <= m; i++) {
		cout << path[i][x] << " ";
		x -= path[i][x];
	}
}