#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 1001;

int t, n;
int A[N], dp[2][N][N];

int go(int p, int l, int r) {
	if (l == r) {
		if (p) return A[l];
		else return 0;
	}

	int& ret = dp[p][l][r];
	if (ret != -1) return ret;

	ret = 0;
	if (p) ret = max(go(0, l + 1, r) + A[l], go(0, l, r - 1) + A[r]);
	else ret = min(go(1, l + 1, r), go(1, l, r - 1));

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> t;
	while (t--) {
		memset(A, 0, sizeof(A));
		memset(dp, -1, sizeof(dp));
		
		cin >> n;
		for (int i = 0; i < n; i++) cin >> A[i];
		
		cout << go(1, 0, n - 1) << endl;
	}
}