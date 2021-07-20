#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 17, MAX = 987654321;
int n, cost[N][N];
ll dp[N][1 << N];

ll go(int x, int visit) {
	if (visit == (1 << n) - 1) {
		if (cost[x][0] != 0) return cost[x][0];
		else return MAX;
	}

	ll& ret = dp[x][visit];
	if (ret != -1) return ret;

	ret = MAX;
	for (int i = 0; i < n; i++) {
		if ((visit & (1 << i)) == 0 && cost[x][i] != 0) {
			ret = min(ret, go(i, visit | (1 << i)) + cost[x][i]);
		}
	}

	return ret;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));


	cin >> n;

	for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
		cin >> cost[i][j];
	}

	ll ans = go(0, 1);

	cout << ans << endl;
}