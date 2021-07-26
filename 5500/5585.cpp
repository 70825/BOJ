#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	int n, ans = 0, cost[6] = { 500, 100, 50, 10, 5, 1 };

	cin >> n;
	n = 1000 - n;

	for (auto nx : cost) {
		ans += n / nx;
		n %= nx;
	}

	cout << ans << endl;
}