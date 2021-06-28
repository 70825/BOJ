#include <iostream>
using namespace std;
typedef long long ll;
unsigned long long n;
const int N = 2;
int MOD = 1e6;
ll ans[2][2] = { 0, }, arr[2][2] = { 0, };

void mul(ll A[N][N], ll B[N][N]) {
	ll res[N][N] = { 0, };
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			for (int k = 0; k < N; k++) 
				res[i][j] = (res[i][j] + (A[i][k] * B[k][j])) % MOD;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			A[i][j] = res[i][j];
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n;
	n--;
	for (int i = 0; i < N; i++) ans[i][i] = 1;
	arr[0][0] = 1; arr[0][1] = 1; arr[1][0] = 1;

	while (n) {
		if (n % 2) mul(ans, arr);
		mul(arr, arr);
		n /= 2;
	}

	cout << ans[0][0];
}