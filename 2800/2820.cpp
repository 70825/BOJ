#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n,m,z=-1;
int cost[500001],Start[500001],End[500001];
vector<int> children[500001];

void dfs(int x){
    z+=1;
    Start[x]=z;
    for(int i=0;i<children[x].size();i++){
        dfs(children[x][i]);
    }
    End[x]=z;
}

struct SegTree{
    vector<ll> tree,lazy;
    SegTree(int x){
        int h = (int)ceil(log2(x));
        tree.resize(1<<(h+1),0);
        lazy.resize(1<<(h+1),0);
    }
    void lazy_update(int now, int s, int e){
        if(lazy[now]!=0) {
            tree[now] += lazy[now] * (e - s + 1);
            if (s != e) {
                lazy[now * 2] += lazy[now];
                lazy[now * 2 + 1] += lazy[now];
            }
            lazy[now] = 0;
        }
    }
    ll update(int now, int s, int e, int L, int R, int val){
        lazy_update(now,s,e);
        if(s>R || e<L) return tree[now];
        if(L<=s && e<=R){
            lazy[now]+=val;
            lazy_update(now,s,e);
            return tree[now];
        }
        int mid=(s+e)/2;
        return tree[now]=update(now*2,s,mid,L,R,val)+update(now*2+1,mid+1,e,L,R,val);
    }
    ll Find(int now,int s,int e,int idx){
        lazy_update(now,s,e);
        if(idx<s || idx>e) return 0;
        if(s==e) return tree[now];
        int mid=(s+e)/2;
        return Find(now*2,s,mid,idx)+Find(now*2+1,mid+1,e,idx);
    }
};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m;
    SegTree ST(n);
    for(int i=0; i<n;i++){
        if(i==0){
            cin >> cost[i];
            continue;
        }
        else{
            int a,b;
            cin >> a >> b;
            cost[i]=a;
            children[b-1].push_back(i);
        }
    }
    dfs(0);
    for(int i=0; i<n; i++) ST.update(1,0,n-1,Start[i],Start[i],cost[i]);
    for(int i=0; i<m; i++){
        char a;
        int b,c;
        cin >> a;
        if(a=='p'){
            cin >> b >> c;
            b-=1;
            ST.update(1,0,n-1,Start[b]+1,End[b],c);
        }
        else{
            cin >> b;
            b-=1;
            cout << ST.Find(1,0,n-1,Start[b]) << "\n";
        }
    }
}