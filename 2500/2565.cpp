#include <iostream>
using namespace std;
typedef long long ll;
const int N = 501;

int main()
{
	int n, x, y;
	cin >> n;

	ll arr[N] = { 0, };
	ll dp[N] = { 0, };

	for (int i = 1; i <= n; i++) {
		cin >> x >> y;
		arr[x] = y;
		dp[x] = 1;
	}
	for (int i = 1; i < N; i++) {
		if (!arr[i]) continue;
		for (int j = 1; j < i; j++) {
			if (arr[i] > arr[j]) dp[i] = max(dp[i], dp[j] + 1);
		}
	}

	ll ans = 0;
	for (int i = 1; i < N; i++) ans = max(ans, dp[i]);
	cout << n - ans;
}