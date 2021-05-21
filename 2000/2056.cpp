#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
const int N = 10002;

int n, num, x;
ll dp[N] = { 0, }, times[N] = { 0, }, finish[N] = { 0, };
vector<vector<ll>> need(N);

ll go(int x) {
	ll& res = dp[x];
	if (res != -1) return res;

	if (need[x].size() == 0) {
		finish[x] = 1;
		return times[x];
	}

	for (auto nx : need[x]) res = max(res, go(nx) + times[x]);
	finish[x] = 1;

	return res;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> times[i] >> num;
		for (int j = 0; j < num; j++) {
			cin >> x;
			need[i].push_back(x);
		}
		dp[i] = -1;
	}
	
	ll ans = 0;
	for (int i = n; i; i--) {
		if (!finish[i]) ans = max(ans, go(i));
	}
	cout << ans;
}