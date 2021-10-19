#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 101, X=10001;
int n, x, arr[N][2], dp[N][X];

int go(int idx, int len) {
	if (len == x) return 1;
	if (idx == n) return 0;

	int& ret = dp[idx][len];
	if (ret != -1) return ret;

	ret = 0;
	for (int i = 0; i <= arr[idx][1]; i++) {
		if (len + arr[idx][0] * i <= x) ret += go(idx + 1, len + arr[idx][0] * i);
	}

	return ret;
}


int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n >> x;
	for (int i = 0; i < n; i++) cin >> arr[i][0] >> arr[i][1];

	cout << go(0, 0) << endl;
}