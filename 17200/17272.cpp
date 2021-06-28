#include <iostream>
#include <cmath>
using namespace std;
typedef long long ll;
const int N = 101;
ll n, m;
ll MOD = 1e9+7;
ll ans[N][N] = { 0, }, arr[N][N] = { 0, };

void mul(ll A[N][N], ll B[N][N]) {
	ll res[N][N] = { 0, };
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			for (int k = 0; k < n; k++) 
				res[i][j] = (res[i][j] + (A[i][k] * B[k][j])) % MOD;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			A[i][j] = res[i][j];
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> m >> n;
	
	for (int i = 0; i < n; i++) ans[i][i] = 1;
	arr[n - 1][0] = 1; arr[n - 1][n - 1] = 1;
	for (int i = 0; i < n - 1; i++) arr[i][i + 1] = 1;

	while (m) {
		if (m % 2) mul(ans, arr);
		mul(arr, arr);
		m /= 2;
	}
	cout << ans[n-1][n-1];
}