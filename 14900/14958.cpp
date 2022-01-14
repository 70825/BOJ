#include <bits/stdc++.h>
using namespace std;

using ll = long long;
typedef complex<double> base;

void fft(vector<base>& a, bool inv) {
	int n = a.size(), j = 0;
	vector<base> roots(n / 2);
	for (int i = 1; i < n; i++) {
		int bit = (n >> 1);
		while (j >= bit) {
			j -= bit;
			bit >>= 1;
		}
		j += bit;
		if (i < j) swap(a[i], a[j]);
	}
	double ang = 2 * acos(-1) / n * (inv ? -1 : 1);
	for (int i = 0; i < n / 2; i++) {
		roots[i] = base(cos(ang * i), sin(ang * i));
	}

	for (int i = 2; i <= n; i <<= 1) {
		int step = n / i;
		for (int j = 0; j < n; j += i) {
			for (int k = 0; k < i / 2; k++) {
				base u = a[j + k], v = a[j + k + i / 2] * roots[step * k];
				a[j + k] = u + v;
				a[j + k + i / 2] = u - v;
			}
		}
	}
	if (inv) for (int i = 0; i < n; i++) a[i] /= n;
}
vector<int> multiply(vector<int>& v, vector<int>& w) {
	vector<base> fv(v.begin(), v.end()), fw(w.begin(), w.end());
	int n = 2; while (n < v.size() + w.size()) n <<= 1;
	fv.resize(n); fw.resize(n);
	fft(fv, 0); fft(fw, 0);
	for (int i = 0; i < n; i++) fv[i] *= fw[i];
	fft(fv, 1);
	vector<int> ret(n);
	for (int i = 0; i < n; i++) ret[i] = (int)round(fv[i].real());
	return ret;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

	int n, m;
	cin >> n >> m;

	string rps, me;
	cin >> rps;
	cin >> me;

	vector<int> rpsR(n), rpsP(n), rpsS(n), meR(m), meP(m), meS(m);

	for (int i = 0; i < n; i++) {
		if (rps[i] == 'R') rpsR[i] = 1;
		if (rps[i] == 'P') rpsP[i] = 1;
		if (rps[i] == 'S') rpsS[i] = 1;
	}
	for (int i = 0; i < m; i++) {
		if (me[i] == 'R') meR[i] = 1;
		if (me[i] == 'P') meP[i] = 1;
		if (me[i] == 'S') meS[i] = 1;
	}

	reverse(meR.begin(), meR.end());
	reverse(meP.begin(), meP.end());
	reverse(meS.begin(), meS.end());

	vector<int> winR = multiply(meR, rpsS), winP = multiply(meP, rpsR), winS = multiply(meS, rpsP);

	int ans = 0;
	for (int i = m - 1; i < n + m - 1; i++) {
		ans = max(ans, winR[i] + winP[i] + winS[i]);
	}

	cout << ans << endl;
	return 0;
}