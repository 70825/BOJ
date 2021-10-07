#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 1001;
int n, arr[N], dp_up[N], dp_down[N];


int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	memset(dp_up, -1, sizeof(dp_up));
	memset(dp_down, -1, sizeof(dp_down));

	cin >> n;
	for (int i = 0; i < n; i++) cin >> arr[i];

	for (int i = 0; i < n; i++) {
		dp_down[i] = 1;
		for (int j = 0; j < i; j++) {
			if (arr[j] > arr[i]) dp_down[i] = max(dp_down[i], dp_down[j] + 1);
		}
	}
	for(int i = n-1; i >= 0; i--){
		dp_up[i] = 1;
		for (int j = n-1; j > i; j--) {
			if (arr[j] > arr[i]) dp_up[i] = max(dp_up[i], dp_up[j] + 1);
		}
	}

	int ans = 0;
	for (int i = 0; i < n; i++) {
		ans = max(ans, dp_down[i] + dp_up[i] - 1);
	}

	cout << ans << endl;
}