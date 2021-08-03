#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

const int N = 1e6 + 1;
int t, n, visit[N];
vector<int> arr;
vector<pair<int, int>> max_val;

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	
	cin >> t;
	while (t--) {
		cin >> n;
		
		arr.resize(n);
		max_val.resize(n);
		memset(visit, 0, sizeof(visit));

		for (int i = 0; i < n; i++) {
			cin >> arr[i];
			max_val[i] = make_pair(arr[i], i);
		}

		sort(max_val.begin(), max_val.end());
        
        long long ans = 0;
		int j = n - 1;

		for (int i = 0; i < n; i++) {
			visit[i] = 1;
			if (max_val[j].second != i) ans += max_val[j].first - arr[i];
			else {
				while (j >= 0 && visit[max_val[j].second]) j--;
			}
		}

		cout << ans << "\n";
	}

	return 0;
}