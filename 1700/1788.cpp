#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1e6+1;
int MOD = 1e9;

int main()
{
	int n;
	cin >> n;

	ll dp_p[N] = { 0, }; dp_p[1] = 1;
	int dp_m[N] = { 0, }; dp_m[1] = 1;

	for (int i = 2; i < N; i++) {
		dp_p[i] = (dp_p[i - 1] + dp_p[i - 2]) % MOD;
		dp_m[i] = (dp_m[i - 2] - dp_m[i - 1]) % MOD;
	}

	if (n > 0) cout << 1 << endl << dp_p[n];
	else if (n == 0) cout << 0 << endl << 0;
	else {
		if (dp_m[-n] > 0) cout << 1 << endl << dp_m[-n];
		else cout << -1 << endl << -dp_m[-n];
	}
}