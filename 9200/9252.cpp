#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 1001;
ll dp[N][N] = { 0, };
string A, B;

void go(int x, int y) {
	if (!dp[x][y]) return;
	if (A[x-1] == B[y-1]) {
		go(x - 1, y - 1);
		cout << A[x-1];
	}
	else {
		if (dp[x - 1][y] >= dp[x][y - 1]) go(x - 1, y);
		else go(x, y - 1);
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> A >> B;

	ll ans = 0;
	for (int i = 1; i <= A.size(); i++) {
		for (int j = 1; j <= B.size(); j++) {
			if (A[i - 1] == B[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
			else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
			ans = max(ans, dp[i][j]);
		}
	}

	cout << ans << endl;
	if (ans) go(A.size(),B.size());
}