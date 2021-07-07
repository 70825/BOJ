#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 502;

int t, n;
int dp[N][N], cost[N], pcost[N];

int go(int x, int y) {
	int& ret = dp[x][y];
	if (ret != -1) return dp[x][y];

	if (y - x == 1) return ret = cost[x] + cost[y];

	ret = min(go(x + 1, y), go(x, y - 1));
	for (int i = x+1; i < y-1; i++) {
		ret = min(ret, go(x, i) + go(i + 1, y));
	}
	ret += pcost[y] - pcost[x - 1];
	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> t;
	while (t--) {
		memset(dp, -1, sizeof(dp));
		memset(cost, 0, sizeof(cost));
		memset(pcost, 0, sizeof(pcost));

		cin >> n;
		for (int i = 1; i <= n; i++) {
			cin >> cost[i];
			pcost[i] = pcost[i - 1] + cost[i];
		}

		cout << go(1, n) << endl;
	}
}