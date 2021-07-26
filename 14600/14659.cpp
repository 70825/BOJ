#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	int n, ans = 0, arr[30001];

	cin >> n;
	for (int i = 0; i < n; i++) cin >> arr[i];

	int x = 0, val = 0;
	for (int i = 1; i < n; i++) {
		if (arr[x] > arr[i]) val += 1;
		else {
			ans = max(ans, val);
			val = 0;
			x = i;
		}
	}

	cout << max(ans, val) << endl;
}