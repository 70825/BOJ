#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 201;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int n;
	cin >> n;

	ll arr[N] = { 0, }, dp[N] = { 0, };
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		dp[i] = 1;
	}

	ll ans = 0;
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (arr[i] > arr[j]) dp[i] = max(dp[i], dp[j] + 1);
		}
		ans = max(ans, dp[i]);
	}

	cout << n - ans;
}