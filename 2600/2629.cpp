#include <iostream>
#include <cstring>
#include <string>
using namespace std;
using ll = long long;

const int N = 31, M = 30001;

int n, m, t;
int cost[N], visit[N][M];

void go(int x, int val) {
	if (x == n) return;
	if (!visit[x][val]) {
		visit[x][val] = 1;
		go(x + 1, val);
	}
	if (!visit[x][val - cost[x]]) {
		visit[x][val - cost[x]] = 1;
		go(x + 1, val - cost[x]);
	}
	if (!visit[x][val + cost[x]]) {
		visit[x][val + cost[x]] = 1;
		go(x + 1, val + cost[x]);
	}
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	for (int i = 0; i < n; i++) cin >> cost[i];
	go(0, 15000);

	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> t;
		if (t > 15000) {
			cout << "N" << " ";
			continue;
		}
		if (visit[n-1][t+15000]) cout << "Y" << " ";
		else cout << "N" << " ";
	}

}