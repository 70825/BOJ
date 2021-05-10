#include <iostream>
using namespace std;
const int N  = 1e6 + 1;

int main()
{
	int dp[N] = { 0, };
	dp[1] = 1;
	dp[2] = 2;
	int n;
	cin >> n;
	for (int i = 3; i < N; i++) {
		dp[i] = (dp[i - 1] + dp[i - 2]) % 15746;
	}
	cout << dp[n];
}