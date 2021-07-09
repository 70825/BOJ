#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

const int N = 10001;
int n, x, y, val[N], dp[N][2];
vector<int> adj[N];

int go(int x, int good, int prev) {
	int& ret = dp[x][good];
	if (ret != -1) return ret;

	ret = good ? val[x] : 0;
	for (auto nx : adj[x]) {
		if (nx != prev) ret += good ? go(nx, 0, x) : max(go(nx, 0, x), go(nx, 1, x));
	}

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n;
	for (int i = 0; i < n; i++) cin >> val[i];
	for (int i = 0; i < n - 1; i++) {
		cin >> x >> y; x--; y--;
		adj[x].push_back(y);
		adj[y].push_back(x);
	}

	cout << max(go(0, 0, -1), go(0, 1, -1)) << endl;
}