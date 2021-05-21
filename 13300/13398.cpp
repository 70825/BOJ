#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 1e5+1;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	ll arr[N] = { 0, }, dp[N][2] = { 0, };

	cin >> n;

	for (int i = 0; i < n; i++) cin >> arr[i];

	ll ans = arr[0];
	dp[0][0] = arr[0]; dp[0][1] = arr[0];
	for (int i = 1; i < n; i++) {
		dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i]);
		dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i]);
		ans = max(ans, max(dp[i][0], dp[i][1]));
	}
	cout << ans;
}