#include <iostream>
#include <cstring>
#include <string>
using namespace std;
using ll = long long;

const int N = 16, MAX = 1e9;

int n, e, s = 0;
int cost[N][N], dp[1 << N];
string state;

int bit(int val) {
	int ans = 0;
	while (val != 0) {
		ans += (val & 1);
		val = val >> 1;
	}
	return ans;
}

int go(int visit) {
	if (bit(visit) >= e) return 0;
	int& ret = dp[visit];
	if (ret != -1) return ret;

	ret = MAX;
	for (int i = 0; i < n; i++) {
		if ((visit & (1 << i))) {
			for (int j = 0; j < n; j++) {
				if (!(visit & (1 << j))) {
					int next = visit | (1 << j);
					ret = min(ret, go(next) + cost[i][j]);
				}
			}
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
	for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) cin >> cost[i][j];
	
	cin >> state;
	for(int i = 0; i < n; i++)
		if (state[i] == 'Y') s |= (1 << i);
	
	cin >> e;
	if (bit(s) == 0) {
		if (e == 0)cout << 0 << endl;
		else cout << -1 << endl;
	}
	else {
		int ans = go(s);
		cout << ans << endl;
	}
}