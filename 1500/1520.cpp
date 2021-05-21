#include <iostream>
using namespace std;
typedef long long ll;
const int N = 501;
ll dx[4] = { 1,-1,0,0 }, dy[4] = { 0,0,1,-1 };

ll m, n;
ll dp[N][N] = { 0, }, arr[N][N] = { 0, };

ll go(ll x, ll y) {

	ll& res = dp[x][y];
	if (dp[x][y] != -1) return res;

	res = 0;
	for (int i = 0; i < 4; i++) {
		ll nx = x + dx[i], ny = y + dy[i];
		if (0 <= nx && nx < m && 0 <= ny && ny < n && arr[x][y] > arr[nx][ny]) res += go(nx, ny);
	}

	return res;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> m >> n;
	for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) {
		cin >> arr[i][j];
		dp[i][j] = -1;
	}

	dp[m - 1][n - 1] = 1;
	cout << go(0, 0);
	
}