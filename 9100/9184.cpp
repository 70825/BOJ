#include <iostream>
using namespace std;
typedef long long ll;
const int N = 21;

int main()
{
	int a, b, c;
	ll dp[N][N][N] = { 0, };
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++) {
				if (i == 0 || j == 0 || k == 0) dp[i][j][k] = 1;
				else if (i < j && j < k) dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k];
				else dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1];
			}
		}
	}

	while (1) {
		cin >> a >> b >> c;
		if (a == b && b == c && c == -1) break;
		cout << "w(" << a << ", " << b << ", " << c << ") = ";
		if (a <= 0 || b <= 0 || c <= 0) cout << 1;
		else if (a > 20 || b > 20 || c > 20) cout << dp[20][20][20];
		else cout << dp[a][b][c];
		cout << endl;
	}
}