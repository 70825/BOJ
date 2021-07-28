#include <iostream>
using namespace std;
typedef long long ll;

const int N = 1e5 + 1;
int n, m, t;
int arr[N], min_tree[4 * N], max_tree[4 * N];

 int min_update(int now, int s, int e, int idx, int val) {
    if (s > idx || e < idx) return min_tree[now];
    if (s == e) return min_tree[now] = val;
    int mid = (s + e) / 2;
    return min_tree[now] = min(min_update(now * 2, s, mid, idx, val), min_update(now * 2 + 1, mid + 1, e, idx, val));
 }

int max_update(int now, int s, int e, int idx, int val) {
    if (s > idx || e < idx) return max_tree[now];
    if (s == e) return max_tree[now] = val;
    int mid = (s + e) / 2;
    return max_tree[now] = max(max_update(now * 2, s, mid, idx, val), max_update(now * 2 + 1, mid + 1, e, idx, val));
}

int find_min(int now, int s, int e, int L, int R) {
    if (R<s || L>e) return 987654321;
    if (L <= s && e <= R) return min_tree[now];
    int mid = (s + e) / 2;
    return min(find_min(now * 2, s, mid, L, R), find_min(now * 2 + 1, mid + 1, e, L, R));
}

int find_max(int now, int s, int e, int L, int R) {
    if (R<s || L>e) return 0;
    if (L <= s && e <= R) return max_tree[now];
    int mid = (s + e) / 2;
    return max(find_max(now * 2, s, mid, L, R), find_max(now * 2 + 1, mid + 1, e, L, R));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> t;
    while (t--) {
        cin >> n >> m;

        for (int i = 0; i < n; i++) {
            arr[i] = i;
            min_update(1, 0, n - 1, i, i);
            max_update(1, 0, n - 1, i, i);
        }

        for (int i = 0; i < m; i++) {
            int a, b, c;
            cin >> a >> b >> c;
            if (a == 0) {
                min_update(1, 0, n - 1, b, arr[c]);
                max_update(1, 0, n - 1, b, arr[c]);
                min_update(1, 0, n - 1, c, arr[b]);
                max_update(1, 0, n - 1, c, arr[b]);
                int x = arr[b];
                arr[b] = arr[c];
                arr[c] = x;
            }
            else {
                int x = find_min(1, 0, n - 1, b, c);
                int y = find_max(1, 0, n - 1, b, c);
                if (x == b && y == c) cout << "YES" << '\n';
                else cout << "NO" << '\n';
            }
        }
    }
}