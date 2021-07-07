#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 501;

int n, r, c;
int dp[N][N], mat_r[N], mat_c[N];

int go(int x, int y) {
	int& ret = dp[x][y];
	if (ret != -1) return dp[x][y];

	if (y - x == 1) return ret = mat_r[x] * mat_c[x] * mat_c[y];

	ret = min(mat_r[x] * mat_c[x] * mat_c[y] + go(x + 1, y), mat_r[x] * mat_r[y] * mat_c[y] + go(x, y - 1));
	for (int i = x+1; i < y-1; i++) {
		ret = min(ret, mat_r[x] * mat_c[i] * mat_c[y] + go(x, i) + go(i+1, y));
	}

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n;
	for (int i = 0; i < n; i++) cin >> mat_r[i] >> mat_c[i];

	cout << go(0, n - 1) << endl;
}