#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 101;
const int MAX = 21;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	ll arr[N] = { 0, }, dp[N][MAX] = { 0, };

	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) cin >> arr[i];

	dp[1][arr[1]] = 1;
	for (int i = 2; i < n; i++) {
		for (int j = 0; j < MAX; j++) {
			if (j - arr[i] >= 0) dp[i][j] += dp[i - 1][j - arr[i]];
			if (j + arr[i] <= 20) dp[i][j] += dp[i - 1][j + arr[i]];
		}
	}

	cout << dp[n - 1][arr[n]];
	
}