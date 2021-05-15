#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1e3+1;

int main()
{
	int a, b, c;
	ll dp_x[N] = { 0, }, dp_y[N] = { 0, };
	dp_x[1] = 1;
	dp_y[0] = 1; dp_y[1] = 1;
	for (int i = 2; i < N; i++) {
		dp_x[i] = dp_x[i - 1] + dp_x[i - 2];
		dp_y[i] = dp_y[i - 1] + dp_y[i - 2];
	}
	while (1) {
		cin >> a >> b >> c;
		if (a == b && b == c && c == 0)break;
		if (c >= 100) {
			cout << 0 << endl;
			continue;
		}
		cout << dp_x[c] * a + dp_y[c] * b << endl;
	}
}