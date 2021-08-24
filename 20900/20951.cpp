#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 1e5 + 1, MOD = 1e9 + 7;
int n, m, u, v;
ll dp[N][8];
vector<int> adj[N];

ll go(int x, int len) {
	if (len > 7) return 1;
	ll& ret = dp[x][len];
	if (ret != -1) return ret;

	ret = 0;
	for (auto nx: adj[x]) {
		ret = (ret + go(nx, len + 1)) % MOD;
	}

	return ret;
}


int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> u >> v;
		adj[--u].push_back(--v);
		adj[v].push_back(u);
	}

	ll ans = 0;
	for (int i = 0; i < n; i++) {
		ans = (ans + go(i, 1)) % MOD;
	}
	cout << ans << endl;
}