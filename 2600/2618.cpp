#include <iostream>
#include <cstring>
#include <string>
using namespace std;
using ll = long long;

const int N = 1002;
int n, w;
pair<int, int> path[N];
ll dp[N][N], who[N][N];

int dist(pair<int, int> a, pair<int, int> b) {
	return abs(a.first - b.first) + abs(a.second - b.second);
}

ll go(int x1, int x2) {
	if (x1 == w || x2 == w) return 0;
	ll& ret = dp[x1][x2];
	if (ret != -1) return ret;

	int p = max(x1, x2) + 1, dist1, dist2;

	dist1 = go(p, x2) + (x1 == 0 ? dist(make_pair(1, 1), path[p]) : dist(path[x1], path[p]));
	dist2 = go(x1, p) + (x2 == 0 ? dist(make_pair(n, n), path[p]) : dist(path[x2], path[p]));
	who[x1][x2] = (dist1 <= dist2) ? 1 : 2;

	ret = min(dist1, dist2);

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n;
	cin >> w;
	for (int i = 1; i <= w; i++) {
		cin >> path[i].first >> path[i].second;
	}

	cout << go(0, 0) << endl;
	int x = 0, y = 0;
	while (x != w && y != w) {
		cout << who[x][y] << endl;
		if (who[x][y] == 1) x = max(x, y) + 1;
		else y = max(x, y) + 1;
	}
}