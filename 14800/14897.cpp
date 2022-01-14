# pragma GCC optimize ("O3")
# pragma GCC optimize ("Ofast")
# pragma GCC optimize ("unroll-loops")
# pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

struct Query {
	int l, r, idx;
};

const int MAX = 1000000;
int n, m, dcnt = 0, sqrtN;
int cnt[MAX + 1] = { 0, }, result[MAX + 1] = { 0, };
vector<Query> q;
vector<int> arr, tmp;

bool compare(Query a, Query b) {
	if (a.l / sqrtN == b.l / sqrtN) return a.r < b.r;
	return a.l / sqrtN < b.l / sqrtN;
}

void sub(int x) {
	cnt[arr[x]]--;
	if (cnt[arr[x]] == 0) dcnt--;
}

void add(int x) {
	if (cnt[arr[x]] == 0) dcnt++;
	cnt[arr[x]]++;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);

	cin >> n; arr.resize(n + 1); sqrtN = int(sqrt(n));
	for (int i = 1; i <= n; i++) cin >> arr[i];
	tmp = arr;
	sort(tmp.begin() + 1, tmp.end());
	tmp.erase(unique(tmp.begin() + 1, tmp.end()), tmp.end());
	for (int i = 1; i <= n; i++) {
		arr[i] = lower_bound(tmp.begin(), tmp.end(), arr[i]) - tmp.begin();
	}

	cin >> m;
	for (int i = 0; i < m; i++) {
		int l, r;
		cin >> l >> r;
		Query qq = { l, r, i };
		q.push_back(qq);
	}

	sort(q.begin(), q.end(), compare);

	int s = q[0].l, e = q[0].r;
	for (int i = s; i < e + 1; i++) add(i);
	result[q[0].idx] = dcnt;

	for (int i = 1; i < m; i++) {
		int qs = q[i].l, qe = q[i].r, idx = q[i].idx;
		while (s < qs)sub(s++);
		while (s > qs)add(--s);
		while (e < qe)add(++e);
		while (e > qe)sub(e--);
		result[idx] = dcnt;
	}

	for (int i = 0; i < m; i++) {
		cout << result[i] << "\n";
	}
}