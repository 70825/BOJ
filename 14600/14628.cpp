#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 101;
int n, m, k, arr[N][2], dp[N][N];

int go(int idx, int hp) {
	if (hp == 0) return 0;
	if (idx == n) return 987654321;

	int& ret = dp[idx][hp];
	if (ret != -1) return ret;

	ret = 987654321;
	for (int i = 0; arr[idx][1] * i <= hp; i++) {
		ret = min(ret, go(idx + 1, hp - arr[idx][1] * i) + arr[idx][0] * i + k * (i - 1) * i / 2);
	}

	return ret;
}


int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n >> m >> k;
	for (int i = 0; i < n; i++) cin >> arr[i][0] >> arr[i][1];

	cout << go(0, m) << endl;
}