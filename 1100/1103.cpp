#include <iostream>
#include <cstring>
#include <string>
using namespace std;
using ll = long long;

const int N = 51;

int n, m;
char p;
int visit[N][N], dp[N][N];
string arr[N][N];
int dx[4] = { 1, -1, 0, 0 }, dy[4] = { 0, 0, -1, 1 };

int go(int x, int y) {
	if (x < 0 || x >= n || y < 0 || y >= m) return -2500;
	if (arr[x][y] == "H") return -2500;
	int& ret = dp[x][y];
	if (visit[x][y]) {
		cout << -1 << endl;
		exit(0);
	}
	if (dp[x][y] != -1) return ret;
	if (arr[x][y] == "H") return -2500;

	int z = stoi(arr[x][y]);
	ret = 1;

	visit[x][y] = 1;
	for (int i = 0; i < 4; i++) ret = max(ret, go(x + z * dx[i], y + z * dy[i]) + 1);
	visit[x][y] = 0;
	return ret;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp, -1, sizeof(dp));

	cin >> n >> m;
	for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
		cin >> p;
		arr[i][j] = p;
	}

	cout << go(0, 0) << endl;

}