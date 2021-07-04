#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;

const int N = 1e6 + 1;
int dp[N], visit[N];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	int n, x, ans = 0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> x;
		visit[x] = 1;
		if (visit[x - 1]) dp[x] = dp[x - 1] + 1;
		else dp[x] = 1;

		ans = max(ans, dp[x]);
	}

	cout << n - ans << endl;
}
