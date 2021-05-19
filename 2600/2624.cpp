#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int T = 10001, K = 101;
ll dp[T][K] = { 0, }, P[K] = { 0, }, N[K] = { 0, };
int t, k;

ll go(int x, int y) {
	if (x == 0) return 1;
	if (x < 0 || y > k) return 0;

	ll& res = dp[x][y];
	if (res != -1) return dp[x][y];

	res = 0;
	for (int i = 0; i <= N[y]; i++) {
		if (x - i * P[y] >= 0)
			res += go(x - i * P[y], y + 1);
	}

	return res;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> t >> k;

	for (int i = 1; i <= k; i++) cin >> P[i] >> N[i];

	for (int i = 0; i < T; i++) for (int j = 0; j < K; j++)dp[i][j] = -1;

	cout << go(t, 1);
}