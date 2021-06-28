#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
const int N = 1001;

ll t, n, k, x, y, num;
ll dp[N], times[N];
vector<int> need[N];

ll go(int x) {
	ll& ret = dp[x];
	if (ret != -1) return ret;

	ret = 0;
	for (int i = 0; i < need[x].size(); i++) {
		ret = max(ret, go(need[x][i]));
	}
	ret += times[x];

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> t;
	while (t--) {
		cin >> n >> k;

		for (int i = 1; i <= n; i++) {
			cin >> times[i];
			need[i].clear();
			dp[i] = -1;
		}

		for (int i = 0; i < k; i++) {
			cin >> x >> y;
			need[y].push_back(x);
		}

		cin >> num;
		cout << go(num) << endl;
	}

	return 0;
}