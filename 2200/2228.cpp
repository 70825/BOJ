#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 101, M = 51;
int MIN = -1e9;

int n, m;
ll arr[N] = { 0, }, dp[N][M] = { 0, }, visit[N][M] = { 0, };

ll go(int x, int y) {
	if (y == 0) return 0;
	if (x > n) return MIN;

	if (visit[x][y]) return dp[x][y];

	visit[x][y] = 1;
	ll& res = dp[x][y];
	res = max(res, go(x + 1, y));
	for (int i = 0; x + i <= n; i++) {
		res = max(res, go(x + i + 2, y - 1) + arr[x + i] - arr[x - 1]);
	}

	return res;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n >> m;

	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
		arr[i] += arr[i - 1];
		for (int j = 1; j <= n / 2 + 1; j++) dp[i][j] = MIN;
	}
	cout << go(1, m);
}