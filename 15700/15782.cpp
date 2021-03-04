#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n,m,i,t=-1,a,b,c;
const int Max=100001;
int s[Max], e[Max];
int check[Max];
vector<int> node[Max];

struct Segment{
    vector<ll> tree,lazy;
    Segment(int x){
        int h = (int)ceil(log2(x));
        tree.resize(1<<(h+1),0);
        lazy.resize(1<<(h+1),0);
    }
    void lazy_update(int now, int s, int e){
        if(lazy[now]==0) return;
        tree[now]^=lazy[now]*((e-s+1)%2);
        if(s!=e){
            lazy[now*2]^=lazy[now];
            lazy[now*2+1]^=lazy[now];
        }
        lazy[now]=0;
    }
    ll update(int now, int s, int e, int L, int R, int val){
        lazy_update(now,s,e);
        if (s>R || e<L) return tree[now];
        if (L<=s && e<=R){
            lazy[now]^=val;
            lazy_update(now,s,e);
            return tree[now];
        }
        int mid=(s+e)/2;
        return tree[now]=update(now*2,s,mid,L,R,val)^update(now*2+1,mid+1,e,L,R,val);
    }
    ll find(int now, int s, int e, int L, int R){
        lazy_update(now,s,e);
        if(R<s || L>e) return 0;
        if(L<=s && e<=R) return tree[now];
        int mid=(s+e)/2;
        return find(now*2,s,mid,L,R)^find(now*2+1,mid+1,e,L,R);
    }
};

void dfs(int x){
    s[x]=++t;
    check[x]=1;
    for(auto nx:node[x]){
        if(check[nx]==0) dfs(nx);
    }
    e[x]=t;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    memset(s,0,sizeof(s));
    memset(e,0,sizeof(e));
    memset(check,0,sizeof(check));
    cin >> n >> m;
    Segment Seg(n);
    for(i=0;i<n-1;i++){
        cin >> a >> b;
        node[a-1].push_back(b-1);
        node[b-1].push_back(a-1);
    }
    dfs(0);
    for(i=0;i<n;i++){
        cin >> a;
        Seg.update(1,0,n-1,s[i],s[i],a);
    }
    for(i=0;i<m;i++){
        cin >> a >> b;
        b-=1;
        if(a==1){
            cout << Seg.find(1,0,n-1,s[b],e[b]) << "\n";
        }
        else{
            cin >> c;
            Seg.update(1,0,n-1,s[b],e[b],c);
        }
    }
}