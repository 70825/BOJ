#include <iostream>
#include <cstring>
#include <vector>
#include <tuple>
using namespace std;
using ll = long long;
using ti = tuple<int, int, int>;

const int N = 101, M = 10001, MAX = 987654321;
int T, n, m, k, u, v, c, d;
vector<ti> adj[N];
ll dp[N][M];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> T;
	while (T--) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) dp[i][j] = MAX;
			adj[i].clear();
		}

		cin >> n >> m >> k;
		for (int i = 0; i < k; i++) {
			cin >> u >> v >> c >> d; // c: 비용, d: 시간
			u--; v--;
			adj[u].push_back(make_tuple(v, c, d));
		}

		dp[0][0] = 0;
		for (int cost = 0; cost < M; cost++) for (int x = 0; x < n; x++) {
			if (dp[x][cost] != MAX) {
				for (auto nt : adj[x]) {
					int nx = get<0>(nt), nc = get<1>(nt), nd = get<2>(nt);
					if(cost + nc <= m) dp[nx][cost + nc] = min(dp[nx][cost + nc], dp[x][cost] + nd);
				}
			}
		}

		ll ans = MAX;
		for (int i = 0; i <= m; i++) {
			ans = min(ans, dp[n - 1][i]);
		}
		
		if (ans == MAX) cout << "Poor KCM" << endl;
		else cout << ans << endl;
	}
	
}