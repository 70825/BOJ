#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1500002;
int t[N] = { 0, }, p[N] = { 0, }, dp[N] = { 0, };
int n;

int go(int x, int score) {
	if (x > n) return 0;

	if (dp[x] != 0) return dp[x];

	int res = go(x+1, score);
	if (x + t[x] <= n+1) res = max(res, go(x + t[x], score) + p[x]);
	dp[x] = res;

	return res;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;
	for (int i = 1; i <= n; i++) cin >> t[i] >> p[i];

	cout << go(1, 0);
	
}