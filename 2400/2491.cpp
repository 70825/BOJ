#include <iostream>
using namespace std;
const int N = 1e6 + 1;

int main()
{
	int n, ans = 1;
	cin >> n;
	
	int arr[N] = { 0, };
	for (int i = 1; i < n; i++) cin >> arr[i];

	int dp1[N] = { 0, }, dp2[N] = { 0, };
	dp1[1] = 1;
	dp2[1] = 1;
	for (int i = 2; i <= n; i++) {
		if (arr[i] >= arr[i - 1]) dp1[i] = dp1[i - 1] + 1;
		else dp1[i] = 1;
		ans = max(ans, dp1[i]);

		if (arr[i] <= arr[i - 1]) dp2[i] = dp2[i - 1] + 1;
		else dp2[i] = 1;
		ans = max(ans, dp2[i]);
	}

	cout << ans;
}