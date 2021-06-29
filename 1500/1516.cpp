#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
typedef long long ll;
const int N = 501;

ll t, n, k, x, num;
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
	memset(dp, -1, sizeof(dp));

	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> times[i];
		cin >> x;
		while (x != -1) {
			need[i].push_back(x);
			cin >> x;
		}
	}

	for (int i = 1; i <= n; i++) {
		cout << go(i) << endl;
	}

	return 0;
}