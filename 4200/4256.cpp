#include <bits/stdc++.h>
using namespace std;

int pre[1001],in[1001],lc[1001],rc[1001];

void go(int px,int pe, int ix, int ie){
    int root_post = pre[px], root_in = -1;

    if(px==pe || px>pe) return;
    for(int i=0; i<=ie-ix; i++){
        if(in[ix+i] == root_post){
            root_in = ix+i;
            break;
        }
    }

    if(root_in - ix != 0) lc[root_post] = pre[px+1];
    if(root_in - ie != 0) rc[root_post] = pre[px+(root_in-ix)+1];

    go(px+1,px+root_in-ix,ix,root_in-1);
    go(px+root_in-ix+1,pe,root_in+1,ie);
}

void print_post(int x){
    if(lc[x]!=-1) print_post(lc[x]);
    if(rc[x]!=-1) print_post(rc[x]);
    cout << x+1 << " ";
}

int main(){
    int t;
    cin >> t;

    while(t--){
        int n, x;
        cin >> n;
        memset(pre,-1,sizeof(pre));
        memset(in,-1,sizeof(in));
        memset(lc,-1,sizeof(lc));
        memset(rc,-1,sizeof(rc));

        for(int i=0; i<n; i++){
            cin >> x;
            pre[i] = x - 1;
        }
        for(int i=0; i<n; i++){
            cin >> x;
            in[i] = x-1;
        }

        go(0,n-1, 0,n-1);
        print_post(pre[0]);
        cout << endl;
    }
}