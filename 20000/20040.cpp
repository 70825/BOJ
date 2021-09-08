#include <iostream>
#include <cstring>
using namespace std;
using ll = long long;

const int N = 500001;
int n, m, a, b, ans = 0;
int p[N];

int find(int x) {
	if (p[x] == x) return x;
	p[x] = find(p[x]);
	return p[x];
}

void merge(int x, int y) {
	x = find(x);
	y = find(y);
	p[y] = p[x];
}

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> n >> m;
	for (int i = 0; i < n; i++) p[i] = i;

	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		if (ans == 0 && find(a) == find(b)) ans = i + 1;
		merge(a, b);
	}

	cout << ans << endl;
}