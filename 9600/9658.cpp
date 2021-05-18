#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1001;

int main()
{
	int n;
	cin >> n;

	ll dp[N] = { 0, }; // dp[x] = 1 무조건 짐
	dp[1] = 1; dp[3] = 1;

	for (int i = 5; i < N; i++) {
		if (!dp[i - 1] && !dp[i - 3] && !dp[i - 4]) dp[i] = 1;
	}

	if (dp[n]) cout << "CY";
	else cout << "SK";
}