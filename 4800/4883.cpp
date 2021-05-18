#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1e5+1;
const int MAX = 1e9;
int dx[4] = { 1,1,1,0 }, dy[4] = { -1,0,1,1 };

int main()
{
	int n, z = 1;

	while (1) {
		cin >> n;
		if (!n) break;

		ll arr[N][3] = { 0, };
		ll dp[N][3] = { 0, };
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < 3; j++) {
				cin >> arr[i][j];
				dp[i][j] = MAX;
			}
		}
		dp[0][1] = arr[0][1];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < 3; j++) {
				for (int k = 0; k < 4; k++) {
					int nx = i + dx[k], ny = j + dy[k];
					if (0 <= nx && nx < n && 0 <= ny && ny < 3) dp[nx][ny] = min(dp[nx][ny], dp[i][j] + arr[nx][ny]);
				}
			}
		}
		cout << z << ". " << dp[n - 1][1] << endl;
		z++;
	}
}