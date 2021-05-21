#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 101;

string p, A[2];
ll dp[N][2][101] = { 0, };

ll go(int x, int y, int z) {
	
	ll& res = dp[x][y][z];
	if (res != -1) return res;

	res = 0;
	for (int i = x + 1; i < A[0].size(); i++) {
		if (A[(y + 1) % 2][i] == p[z + 1]) res += go(i, (y + 1) % 2, z + 1);
	}
	return res;
}


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> p >> A[0] >> A[1];

	memset(dp, -1, sizeof(dp));
	for (int i = 0; i < A[0].size(); i++) {
		for (int j = 0; j < 2; j++) {
			if (p[p.size() - 1] == A[j][i]) dp[i][j][p.size() - 1] = 1;
		}
	}

	ll ans = 0;
	for (int i = 0; i < A[0].size(); i++) {
		for (int j = 0; j < 2; j++) {
			if (p[0] == A[j][i]) ans += go(i, j, 0);
		}
	}
	cout << ans;
}