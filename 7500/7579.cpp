#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 101, M = 1e7;
ll memory[N], cost[N], dp[N][10001];

int n, m;

ll go(int x, int left_cost) {
	if (x == n) return 0;

	ll& ret = dp[x][left_cost];
	if (ret != -1) return ret;

	ret = go(x + 1, left_cost);
	if(left_cost >= cost[x]) ret = max(ret, go(x+1, left_cost - cost[x]) + memory[x]);

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));
	
	cin >> n >> m;
	for (int i = 0; i < n; i++) cin >> memory[i];
	for (int i = 0; i < n; i++) cin >> cost[i];

	for (int i = 0; i <= 10000; i++) {
		if (go(0, i) >= m) {
			cout << i << endl;
			break;
		}
	}
}
