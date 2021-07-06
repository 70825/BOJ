#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 2002;

int n, m, x, y;
int A[N], dp[N][N];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	for (int i = 1; i <= n; i++) cin >> A[i];

	// 홀수 길이
	for (int i = 1; i <= n; i++) {
		for (int j = i; j <= i + min(n - i, i - 1); j++) {
			x = i - (j - i); y = j;
			if (A[x] == A[y]) dp[x][y] = 1;
			else break;
		}
	}

	// 짝수 길이
	for (int i = 1; i < n; i++) {
		for (int j = i + 1; j <= i + min(i, n - i); j++) {
			x = i + 1 - (j - i); y = j;
			if (A[x] == A[y]) dp[x][y] = 1;
			else break;
		}
	}

	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> x >> y;
		cout << dp[x][y] << '\n';
	}
}