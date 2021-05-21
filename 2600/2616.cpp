#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 50001;

int n, t;
ll arr[N] = { 0, }, dp[N][3] = { 0, };

ll go(int x, int y) {
	if (y == 3) return 0;
	if (x > n) return -1e9;

	ll& res = dp[x][y];
	if (res != -1) return res;

	res = go(x + 1, y);
	res = max(res, go(x + t, y + 1) + arr[x] - arr[x - t]);

	return res;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
		arr[i] += arr[i - 1];
	}
	cin >> t;

	memset(dp, -1, sizeof(dp));

	cout << go(t-1, 0);
}