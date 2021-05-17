#include <iostream>
using namespace std;
typedef long long ll;
const int N = 31;

int main()
{
	int d, k;
	cin >> d >> k;

	ll x[N] = { 0, }, y[N] = { 0, };
	x[1] = 1; y[2] = 1;
	for (int i = 3; i <= d; i++) {
		x[i] = x[i - 1] + x[i - 2];
		y[i] = y[i - 1] + y[i - 2];
	}

	for (int i = 0; i <= k / x[d]; i++) {
		for (int j = 0; j <= k / y[d]; j++) {
			if (x[d] * i + y[d] * j == k) {
				cout << i << endl << j << endl;
				return 0;
			}
		}
	}
}