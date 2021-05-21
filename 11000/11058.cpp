#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 101;


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	ll dp[N] = { 0, };
	for (int i = 1; i < N; i++) {
		dp[i] = dp[i - 1] + 1;
		for (int j = 3; j < i; j++) dp[i] = max(dp[i], dp[i - j] * (j - 1));
	}
	cout << dp[n];
}