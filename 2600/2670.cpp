#include <iostream>
#include <cstdio>
using namespace std;
const int N  = 10001;

int main()
{
	int n;
	cin >> n;

	double num[N] = { 0, };
	for (int i = 0; i < n; i++) cin >> num[i];

	double ans = 0;
	for (int i = 0; i < n; i++) {
		double x = 1;
		for (int j = i; j < n; j++) {
			x *= num[j];
			ans = max(ans, x);
		}
	}

	printf("%0.3lf", ans);
}