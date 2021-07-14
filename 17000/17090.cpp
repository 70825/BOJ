#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 501;
int n, m, ans = 0;
char MAP[N][N];
int dp[N][N];

int go(int x, int y) {
	if (x < 0 || x >= n || y < 0 || y >= m) return 1;

	int&ret = dp[x][y];
	if (ret != -1) return ret;

	ret = 0;
	if (MAP[x][y] == 'U') ret = go(x - 1, y);
	if (MAP[x][y] == 'D') ret = go(x + 1, y);
	if (MAP[x][y] == 'L') ret = go(x, y - 1);
	if (MAP[x][y] == 'R') ret = go(x, y + 1);

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n >> m;
	for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) cin >> MAP[i][j];

	for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) ans += go(i, j);

	cout << ans << endl;
}