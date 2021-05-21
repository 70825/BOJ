#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 1001;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	ll dp[N] = { 0, };
	for (int i = 2; i < N; i++) dp[i] = 1e9;

	for (int i = 2; i < N; i++) {
		for (int j = 1; j < i; j++) {
			ll x = ((i - j) / j) + (bool)(i % j);
			dp[i] = min(dp[i], dp[j] + 1 + x + (x + 1) * j - i);
		}
	}
	cin >> n;
	cout << dp[n];
}