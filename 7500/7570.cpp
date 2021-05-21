#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 1e6+1;


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	ll arr[N] = { 0, }, dp[N] = { 0, }, idx[N] = { 0, };
	idx[0] = 1e9;

	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
		idx[arr[i]] = i;
	}

	ll ans = 0;
	for (int i = 1; i <= n; i++) {
		if (idx[arr[i]] > idx[arr[i] - 1]) dp[i] = dp[idx[arr[i] - 1]] + 1;
		else dp[i] = 1;
		ans = max(ans, dp[i]);
	}
	cout << n - ans;
}