#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

const int N = 10001;
int n, x, y, cost[N], need[N];
vector<int> adj[N], path;
ll dp[N][2];

ll go(int x, int in, int prev) {
	if (prev != -1 && adj[x].size() == 1) {
		if (in) return cost[x];
		else return 0;
	}
	ll& ret = dp[x][in];
	if (ret != -1) return ret;

	ret = 0;
	for (auto nx : adj[x]) {
		if (nx != prev) {
			if (in) ret += go(nx, 0, x);
			else ret += max(go(nx, 1, x), go(nx, 0, x));
		}
	}

	if (in) ret += cost[x];

	return ret;
}

void find(int x, int prev, int in) {
	if (in) {
		path.push_back(x + 1);
		for (auto nx : adj[x]) {
			if (nx != prev) find(nx, x, 0);
		}
	}
	else {
		for (auto nx : adj[x]) {
			if (nx != prev) {
				if (dp[nx][1] >= dp[nx][0]) find(nx, x, 1);
				else find(nx, x, 0);
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));


	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> cost[i];
	}
	for (int i = 0; i < n - 1; i++) {
		cin >> x >> y;
		adj[--x].push_back(--y);
		adj[y].push_back(x);
	}

	ll ans = max(go(0, 0, -1), go(0, 1, -1));
	if (go(0, 1, -1) > go(0, 0, -1)) need[0] = 1;
	cout << ans << endl;

	find(0, -1, go(0, 1, -1) > go(0, 0, -1) ? 1 : 0);
	sort(path.begin(), path.end());
	for (auto x : path) cout << x << " ";

	cout << dp[5][0] << " " << dp[5][1] << endl;
}