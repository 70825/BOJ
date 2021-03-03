#include <bits/stdc++.h>
using namespace std;

vector<int> lc;
vector<int> rc;
vector<int> in;
vector<int> post;

void DFS(int isx, int iex, int psx, int pex){
    if(isx >= iex) return;
    int root = post[pex], in_root, rc_len, lc_len;

    for(int i=isx; i<=iex; i++){
        if(in[i] == root){
            in_root = i;
            lc_len = i - isx;
            rc_len = iex - i;
            break;
        }
    }

    if(in_root != isx) lc[root] = post[psx + lc_len - 1];
    if(in_root != iex) rc[root] = post[psx + lc_len + rc_len -1];

    DFS(isx, in_root-1, psx, psx + lc_len - 1);
    DFS(in_root + 1, iex, psx + lc_len, pex - 1);
}

void print_pre(int x){
    cout << x+1 << " ";
    if(lc[x] != -1) print_pre(lc[x]);
    if(rc[x] != -1) print_pre(rc[x]);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, x;
    cin >> n;

    lc.resize(n,-1);
    rc.resize(n,-1);
    in.resize(n);
    post.resize(n);

    for(int i=0; i<n; i++){
        cin >> x;
        in[i] = --x;
    }
    for(int i=0; i<n; i++){
        cin >> x;
        post[i] = --x;
    }

    DFS(0,n-1,0,n-1);
    print_pre(post[n-1]);
}