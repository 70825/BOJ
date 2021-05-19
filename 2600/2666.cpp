#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 21;

int n, sx, sy, t;
ll dp[N][N][N] = { 0, }, arr[N];
ll ans = 1e9;

void go(int now, int x, int y, ll val) {
	if (now > t) {
		ans = min(ans, val);
		return;
	}
	dp[now][x][y] = val;

	if (arr[now] == x || arr[now] == y) go(now + 1, x, y, val);
	if (x > 1 && dp[now][x - 1][y] > val + 1) go(now, x - 1, y, val + 1);
	if (x < y - 1 && dp[now][x + 1][y] > val + 1) go(now, x + 1, y, val + 1);
	if (y > x + 1 && dp[now][x][y - 1] > val + 1) go(now, x, y - 1, val + 1);
	if (y < n && dp[now][x][y + 1] > val + 1) go(now, x, y + 1, val + 1);

	return;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n;
	cin >> sx >> sy;

	cin >> t;
	for (int i = 1; i <= t; i++) cin >> arr[i];

	for (int i = 0; i < N; i++)for (int j = 0; j < N; j++)for (int k = 0; k < N; k++) dp[i][j][k] = 1e9;
	
	go(1, sx, sy, 0);
	cout << ans;
}