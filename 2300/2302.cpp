#include <iostream>
using namespace std;
typedef long long ll;
const int N = 41;

int main()
{
	int n, m;
	int vip[N] = { 0, };
	ll dp[N][2] = { 0, }; // 0 : 왼쪽, 1: 가만히

	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int x;
		cin >> x;
		vip[x] = 1;
	}
	
	dp[1][1] = 1;
	for (int i = 2; i <= n; i++) {
		dp[i][1] = dp[i - 1][0] + dp[i - 1][1];
		if (!vip[i - 1] && !vip[i]) dp[i][0] = dp[i - 1][1];
	}
	cout << dp[n][0] + dp[n][1];
}