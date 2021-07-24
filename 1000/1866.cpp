#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;
using ll = long long;

const int N = 3002;
int n, x, t, h;
int psum[N], dp[N];


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	cin >> n;

	vector<int> arr(n + 1);
	for (int i = 1; i <= n; i++) cin >> arr[i];
	sort(arr.begin() + 1, arr.end());

	cin >> t >> h;

	for (int i = 1; i <= n; i++) psum[i] = psum[i - 1] + arr[i] * t;

	for (int i = 1; i <= n; i++) {
		dp[i] = dp[i - 1] + arr[i] * t;
		for (int j = 1; j <= i; j++) {
			int mid = (i + j) / 2;
			
			int left = (arr[mid] * (mid - (j - 1))) * t - (psum[mid] - psum[j - 1]);
			int right = (psum[i] - psum[mid - 1]) - (arr[mid] * (i - mid + 1)) * t;

			dp[i] = min(dp[i], dp[j - 1] + left + right + h);
		}
	}
	
	cout << dp[n] << endl;

	return 0;
}