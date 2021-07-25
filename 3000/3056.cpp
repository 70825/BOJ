#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 21;
double dp[1 << N], s[N][N];
int n;

double go(int x, int visit) {
	if (x == n) return 1.0;

	double& ret = dp[visit];
	if (ret != -1) return ret;

	ret = 0.0;
	for (int i = 0; i < n; i++) {
		if ((visit & (1 << i)) == 0) {
			ret = max(ret, go(x + 1, visit | (1 << i)) * s[x][i]);
		}
	}

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cout << fixed;
	cout.precision(11);
	for (int i = 0; i < (1 << N); i++) dp[i] = -1;

	cin >> n;
	for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
		cin >> s[i][j];
		s[i][j] *= 0.01;
	}
	
	cout << go(0, 0) * 100 << endl;

	return 0;
}