#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 1001;

int n;
int S[N], ic[N], dc[N];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> S[i];
		ic[i] = 1;
		dc[i] = 1;
	}

	for (int i = 0; i < n; i++) for (int j = 0; j < i; j++)
		if (S[i] > S[j]) ic[i] = max(ic[i], ic[j] + 1);
	for (int i = n - 1; i >= 0; i--) for (int j = n - 1; j > i; j--)
		if (S[i] > S[j]) dc[i] = max(dc[i], dc[j] + 1);

	int ans = 0;
	for (int i = 0; i < n; i++) {
		ans = max(ans, ic[i] + dc[i] - 1);
	}
	cout << ans << endl;
}