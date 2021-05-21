#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 1001;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	ll dp[N][N] = { 0, };

	string A, B;
	cin >> A;
	cin >> B;

	ll ans = 0;
	for (int i = 1; i <= A.size(); i++) {
		for (int j = 1; j <= B.size(); j++) {
			if (A[i - 1] == B[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
			else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
			ans = max(ans, dp[i][j]);
		}
	}

	cout << ans;
	
}