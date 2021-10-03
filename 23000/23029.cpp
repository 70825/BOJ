#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 100001;
int n, arr[N];
ll dp[N][3];

ll go(int x, int times) {
	if (x == n) return 0;

	ll& ret = dp[x][times];
	if (ret != -1) return ret;

	ret = 0;
	if (times == 2) ret = max(ret, go(x + 1, 0));
	if (times == 1){
		ll tmp = max(go(x + 1, 0), go(x + 1, 2) + (arr[x] / 2));
		ret = max(ret, tmp);
	}
	if (times == 0) {
		ll tmp = max(go(x + 1, 0), go(x + 1, 1) + arr[x]);
		ret = max(ret, tmp);
	}

	return ret;
}


int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n;
	for (int i = 0; i < n; i++) cin >> arr[i];

	cout << go(0, 0) << endl;

	return 0;
}