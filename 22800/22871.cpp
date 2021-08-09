#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 5001;
int n;
ll arr[N], dp[N];

ll go(int x) {
	if (x == n - 1) return 0;
	ll& ret = dp[x];
	if (ret != -1) return ret;

	ret = 1e10;
	for (int i = x + 1; i < n; i++) {
		ret = min(ret, max(go(i), (i - x) * (1 + abs(arr[x] - arr[i]))));
	}
	return ret;
}


int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n;
	for (int i = 0; i < n; i++) cin >> arr[i];
	
	cout << go(0) << endl;

	return 0;
}