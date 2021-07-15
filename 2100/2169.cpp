#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 1001, MIN = -1e9;
int n, m, MAP[N][N];
ll dp[N][N][4]; // 0 = 아래쪽, 1 = 오른쪽, 2 = 왼쪽

ll go(int x, int y, int dir) {
	if (x < 0 || x >= n || y < 0 || y >= m) return MIN;
	if (x == n - 1 && y == m - 1) return MAP[n - 1][m - 1];

	ll& ret = dp[x][y][dir];
	if (ret != -1) return ret;

	ret = go(x + 1, y, 0);
	if (dir != 1) ret = max(ret, go(x, y - 1, 2));
	if (dir != 2) ret = max(ret, go(x, y + 1, 1));

	ret += MAP[x][y];

	return ret;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));
	
	cin >> n >> m;
	for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
		cin >> MAP[i][j];
	}

	cout << go(0, 0, 0) << endl;
}