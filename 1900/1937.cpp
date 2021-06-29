#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
typedef long long ll;
const int N = 501;

int n, m;
ll ans = 0;
ll dp[N][N], val[N][N];
ll dx[4] = { 1, -1, 0 , 0 }, dy[4] = { 0, 0, 1, -1 };

ll go(int x, int y) {
	ll& ret = dp[x][y];
	if (ret != -1) return ret;

	ret = 1;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i], ny = y + dy[i];
		if (0 <= nx && nx < N && 0 <= ny && ny <= N && val[x][y] < val[nx][ny]) {
			ret = max(ret, go(nx, ny) + 1);
		}
	}

	ans = max(ans, ret);
	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> val[i][j];
		}
	}

	for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
		if (dp[i][j] == -1) go(i, j);
	}

	cout << ans << endl;
	return 0;
}