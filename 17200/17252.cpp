#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
using ll = long long;

const int N = 21;
int n;

int go(int val, int x) {
	if (x == 21) {
		if (val == 0) return 1;
		return 0;
	}

	int ans = 0;
	if (val - pow(3, x) >= 0) ans = max(ans, go(val - pow(3, x), x + 1));
	ans = max(ans, go(val, x + 1));

	return ans;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	
	cin >> n;
	if (n == 0) {
		cout << "NO";
		return 0;
	}
	int res = go(n, 0);
	if (res) cout << "YES" << endl;
	else cout << "NO" << endl;
}