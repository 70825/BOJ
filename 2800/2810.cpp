#include <iostream>
#include <cstring>
#include <string>
using namespace std;
using ll = long long;

const int N = 52;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	int n;
	string s;

	cin >> n;
	cin >> s;

	int x = 0, ans = 0;
	for (int i = 0; i < n;) {
		if (x > n) break;
		if (s[i] == 'S') {
			if (i == x - 1 || i == x) {
				x++; ans++;
			}
			i++;
		}
		if (s[i] == 'L') {
			if (x == i) {
				x += 3; ans += 2;
			}
			if (x == i + 1) {
				x += 2; ans++;
			}
			i += 2;
		}
	}

	cout << ans << endl;
	
}