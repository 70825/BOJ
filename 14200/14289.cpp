#include <iostream>
using namespace std;
typedef long long ll;
const int N = 51;
ll n, m, d;
int MOD = 1e9+7;
ll ans[N][N] = { 0, }, arr[N][N] = { 0, };

void mul(ll A[N][N], ll B[N][N]) {
	ll res[N][N] = { 0, };
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			for (int k = 0; k < n; k++) 
				res[i][j] = (res[i][j] + (A[i][k] * B[k][j])) % MOD;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			A[i][j] = res[i][j];
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n >> m;
	for (int i = 0; i < n; i++) ans[i][i] = 1;
	for (int i = 0; i < m; i++) {
		int x, y;
		cin >> x >> y;
		arr[x - 1][y - 1] = 1;
		arr[y - 1][x - 1] = 1;
	}
	cin >> d;

	while (d) {
		if (d % 2) mul(ans, arr);
		mul(arr, arr);
		d /= 2;
	}

	cout << ans[0][0];
}