#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
typedef long long ll;

const int N = 1e6+1;
vector<int> adj[N];
int dp[N][2];

int go(int x, int e, int p) {
	int& ret = dp[x][e];
	if (ret != -1) return ret;

	ret = e;
	for (auto nx : adj[x]) {
		if (nx == p) continue;
		if (e) ret += min(go(nx, 1, x), go(nx, 0, x));
		else ret += go(nx, 1, x);
	}

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	memset(dp, -1, sizeof(dp));

	int n, u, v;
	cin >> n;
	for (int i = 0; i < n - 1; i++) {
		cin >> u >> v;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	cout << min(go(1, 0, -1), go(1, 1, -1)) << endl;

	return 0;
}