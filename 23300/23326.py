#include <iostream>
#include <cstring>
#include <set>
using namespace std;
using ll = long long;

int n, q, x, y;
bool arr[500001];
set<int> s;

int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);

	cin >> n >> q;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		if (arr[i]) s.insert(i);
	}

	int now = 0;

	for (int i = 0; i < q; i++) {
		cin >> x;
		if (x == 1) {
			cin >> y;
			if (arr[y - 1]) {
				arr[y - 1] = 0;
				s.erase(y - 1);
			}
			else {
				arr[y - 1] = 1;
				s.insert(y - 1);
			}
		}
		else if (x == 2) {
			cin >> y;
			now = (now + y) % n;
		}
		else {
			if (s.empty()) cout << -1 << "\n";
			else if ((*s.rbegin()) >= now) cout << (*s.lower_bound(now)) - now << "\n";
			else cout << n + (*s.begin()) - now << "\n";
		}
	}
}