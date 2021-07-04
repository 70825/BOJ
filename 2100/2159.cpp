#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

int dx[4] = { 1, -1, 0, 0 }, dy[4] = { 0, 0, 1,-1 };
const int N = 1e5+1;
ll X, Y, dp[N][4], p_x[N][4], p_y[N][4];

int n;
ll INF = 1e12;

ll go(int x, int dir) {
	if (x == n-1) return 0;
	ll& ret = dp[x][dir];
	if (ret != -1) return ret;

	ret = INF;
	for (int i = 0; i < 4; i++) {
		ret = min(ret, go(x + 1, i) + abs(p_x[x][dir] - p_x[x + 1][i]) + abs(p_y[x][dir] - p_y[x + 1][i]));
	}

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));
	
	cin >> n;
	cin >> X >> Y;

	int x, y;
	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		for (int j = 0; j < 4; j++) {
			p_x[i][j] = x + dx[j];
			p_y[i][j] = y + dy[j];
		}
	}

	ll ans = INF;
	for (int i = 0; i < 4; i++) {
		ans = min(ans, go(0, i) + abs(X - p_x[0][i]) + abs(Y - p_y[0][i]));
	}

	cout << ans << endl;
}
