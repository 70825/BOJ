#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 101;

int n, m;
ll dp[N][N] = { 0, }, date[N] = { 0, };

ll go(int t, int coupon) {
	if (t >= n) return 0;

	ll& res = dp[t][coupon];
	if (res != -1) return res;

	res = 1e9;
	if (t + 1 <= n && date[t+1]) res = min(res, go(t + 1, coupon));
	if (coupon >= 3) res = min(res, go(t + 1, coupon - 3));
	res = min(res, go(t + 1, coupon) + 10000);
	res = min(res, go(t + 3, coupon + 1) + 25000);
	res = min(res, go(t + 5, coupon + 2) + 37000);

	return res;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		int x;
		cin >> x;
		date[x] = 1;
	}

	for (int i = 0; i < N; i++)for(int j =0; j < N; j++)dp[i][j] = -1;
	cout << go(0, 0);
}