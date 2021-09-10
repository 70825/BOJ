#include <iostream>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
using ll = long long;

const int N = 10001;
int n, a, b, dp[N][3];
string s, t;
vector<char> S, T;
char arr[3];

int go(int x, int idx, int y) {
	if (y == n) {
		if (idx == 2) return 1;
		else return 0;
	}

	int& ret = dp[y][idx];
	if (ret != -1) return ret;

	ret = 0;
	if (x < n - 2 && S[x] == T[y]) ret = max(ret, go(x + 1, idx, y + 1));
	if (idx < 2 && arr[idx] == T[y]) ret = max(ret, go(x, idx + 1, y + 1));

	return ret;
}

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n;
	cin >> s;
	cin >> t;
	cin >> a >> b;

	arr[0] = s.at(a);
	arr[1] = s.at(b);

	for (int i = 0; i < n; i++) {
		if (i == a || i == b) continue;
		S.push_back(s.at(i));
	}
	for (int i = 0; i < n; i++) {
		T.push_back(t.at(i));
	}


	if (go(0, 0, 0)) cout << "YES" << endl;
	else cout << "NO" << endl;
}