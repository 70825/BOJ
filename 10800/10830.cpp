#include <iostream>
using namespace std;
typedef long long ll;
const int N = 6;
ll n, b;
ll ans[N][N] = { 0, }, arr[N][N] = { 0, };

void mul(ll A[N][N], ll B[N][N]) {
	ll res[N][N] = { 0, };
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			for (int k = 0; k < n; k++) 
				res[i][j] = (res[i][j] + (A[i][k] * B[k][j])) % 1000;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			A[i][j] = res[i][j];
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n >> b;
	for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) cin >> arr[i][j];

	for (int i = 0; i < n; i++) ans[i][i] = 1;

	while (b) {
		if (b % 2) mul(ans, arr);
		mul(arr, arr);
		b /= 2;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << ans[i][j] << " ";
		}
		cout << endl;
	}
}