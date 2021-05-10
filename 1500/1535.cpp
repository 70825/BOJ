#include <iostream>
using namespace std;
const int N = 21;
int ans = 0;
int n;
int L[N] = { 0, }, J[N] = { 0, };

void go(int x, int hp, int val) {
	if (x == n) {
		ans = max(ans, val);
		return;
	}
	if (hp > L[x+1]) go(x+1, hp - L[x+1], val + J[x+1]);
	go(x+1, hp, val);
}

int main()
{
	cin >> n;
	for (int i = 0; i < n; i++) cin >> L[i];
	for (int i = 0; i < n; i++) cin >> J[i];

	go(-1, 100, 0);
	cout << ans;

}