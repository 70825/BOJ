#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1e6+1;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;

	int arr[N] = { 0, }, dp[N] = { 0, };
	for (int i = 0; i < N; i++) dp[i] = N;

	arr[1] = -1; dp[1] = 0;
	for (int i = 2; i <= n; i++) {
		if (i % 3 == 0 && dp[i] > dp[i / 3] + 1) {
			arr[i] = i / 3;
			dp[i] = dp[i / 3] + 1;
		}
		if (i % 2 == 0 && dp[i] > dp[i / 2] + 1) {
			arr[i] = i / 2;
			dp[i] = dp[i / 2] + 1;
		}
		if (dp[i] > dp[i - 1] + 1) {
			arr[i] = i - 1;
			dp[i] = dp[i - 1] + 1;
		}
	}

	cout << dp[n] << endl;

	int x = n;
	while (x != -1) {
		cout << x << " ";
		x = arr[x];
	}
}