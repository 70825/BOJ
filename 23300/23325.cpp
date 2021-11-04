#include <iostream>
#include <cstring>
#include <string>
using namespace std;
using ll = long long;

string s;
int dp[200001][7];

int go(int idx, int num) {
	if (idx == s.length()) return 0;

	int& ret = dp[idx][num];
	if (ret != -1) return ret;

	ret = -987654321;
	if (idx + 1 < s.length()) {
		if(s[idx] == '+' && s[idx + 1] == '-') ret = max(ret, go(idx + 2, 1) + 1);
		if(s[idx] == '+' && s[idx + 1] == '+') ret = max(ret, go(idx + 2, 2) + 10);
		if(s[idx] == '-' && s[idx + 1] == '-') ret = max(ret, go(idx + 2, 4) - 1);
		if(s[idx] == '-' && s[idx + 1] == '+') ret = max(ret, go(idx + 2, 5) - 10);
	}
	if (idx + 2 < s.length()) {
		if (s[idx] == '+' && s[idx + 1] == '+' && s[idx + 2] == '-') ret = max(ret, go(idx + 3, 3) + 11);
		if (s[idx] == '-' && s[idx + 1] == '+' && s[idx + 2] == '-') ret = max(ret, go(idx + 3, 6) - 11);
	}
	
	return ret;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> s;

	int ans = -987654321;

	if (0 < s.length()) {
		if (s[0] == '-') ans = max(ans, go(1, 1) + 1);
		if (s[0] == '+') ans = max(ans, go(1, 2) + 10);
	}
	if (1 < s.length()) {
		if (s[0] == '+' && s[1] == '-') ans = max(ans, go(2, 3) + 11);
	}
	cout << ans << endl;
}