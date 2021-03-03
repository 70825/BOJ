#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll init(vector<ll> &tree, vector<ll> &D, int now,int s,int e){
    if(s==e) return tree[now]=D[s];
    else{
        int mid=(s+e)/2;
        return tree[now]=init(tree,D,now*2,s,mid)+init(tree,D,now*2+1,mid+1,e);
    }
}

void update(vector<ll> &tree, int now, int s, int e, int idx, int val){
    if(!(s<=idx && idx<=e)) return;
    tree[now]+=val;
    if(s!=e){
        int mid = (s+e)/2;
        update(tree,now*2,s,mid,idx,val);
        update(tree,now*2+1,mid+1,e,idx,val);
    }
}

ll sum(vector<ll> &tree, int now, int s, int e, int L, int R){
    if(s>R || e<L) return 0;
    if (L<=s && e<=R) return tree[now];
    int mid=(s+e)/2;
    return sum(tree,now*2,s,mid,L,R)+sum(tree,now*2+1,mid+1,e,L,R);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,m,h;
    cin >> n >> m;
    h = (int)ceil(log2(n));
    vector<ll> D(n),tree(1<<(h+1));
    init(tree,D,1,0,n-1);
    while(m--){
        int a,b,c;
        cin >> a >> b >> c;
        if(a==1){
            int val = c-D[b-1];
            D[b-1]=c;
            update(tree,1,0,n-1,b-1,val);
        }
        else {
            if(b>c) swap(b,c);
            cout << sum(tree, 1, 0, n - 1, b - 1, c - 1) << "\n";
        }
    }
}