#include <iostream>
#include <cstring>
#include <string>
using namespace std;
using ll = long long;

const int N = 2501;
string n;
ll dp[N], p[N][N];

ll is_palindrome(int s, int e) {
	ll&ret = p[s][e];
	if (ret != -1) return ret;
	if (s == e) return ret = 1;
	if (n[s] != n[e]) return ret = 0;
	if (s + 1 == e) return ret = 1;
	ret = is_palindrome(s + 1, e - 1);

	return ret;
}

ll go(int x) {
	if (x >= n.size()) return 0;
	ll& ret = dp[x];
	if (ret != -1) return ret;

	ret = 2500;
	for (int i = x; i < n.size(); i++) {
		if (is_palindrome(x, i)) ret = min(ret, go(i + 1) + 1);
	}

	return ret;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));
	memset(p, -1, sizeof(p));

	cin >> n;

	cout << go(0) << endl;
}