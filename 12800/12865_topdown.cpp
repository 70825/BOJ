#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 101, K = 1e5+1;

ll dp[N][K] = { 0, }, W[N] = { 0, }, V[N] = { 0, };
int n, k;

ll go(int now, int capa) {
	if (now > n) return 0;

	ll& res = dp[now][capa];
	if (res != -1) return res;

	res = 0;
	if (capa >= W[now]) res = max(go(now + 1, capa), go(now + 1, capa - W[now]) + V[now]);
	else res = go(now + 1, capa);

	return res;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	for (int i = 1; i < N; i++) for (int j = 1; j < K; j++) dp[i][j] = -1;

	cin >> n >> k;

	for (int i = 1; i <= n; i++) cin >> W[i] >> V[i];
	cout << go(1, k);
}