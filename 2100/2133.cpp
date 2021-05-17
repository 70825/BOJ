#include <iostream>
using namespace std;
typedef long long ll;
const int N = 31;

int main()
{
	int n;
	cin >> n;

	ll dp[N] = { 0, };
	dp[0] = 1;
	dp[2] = 3;
	for (int i = 4; i < N; i += 2) {
		dp[i] = dp[i - 2] * 3;
		for (int j = 4; j <= i; j += 2) dp[i] += dp[i-j] * 2;
	}
	cout << dp[n];
}