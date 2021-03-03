#include <bits/stdc++.h>
using namespace std;

class Tree{
private:
    int N;
    vector<int> lc;
    vector<int> rc;
public:
    Tree(): N(0){}
    Tree(int n): N(n){
        lc.resize(n,-1);
        rc.resize(n,-1);

    }
    void add_sub_tree(int p, int l, int r){
        if(l>0) lc[p] = l;
        if(r>0) rc[p] = r;
    }
    void preorder(int x){
        cout << (char)(x+65);
        if(lc[x] != -1) preorder(lc[x]);
        if(rc[x] != -1) preorder(rc[x]);
    }
    void inorder(int x){
        if(lc[x] != -1) inorder(lc[x]);
        cout << (char)(x+65);
        if(rc[x] != -1) inorder(rc[x]);
    }
    void postorder(int x){
        if(lc[x] != -1) postorder(lc[x]);
        if(rc[x] != -1) postorder(rc[x]);
        cout << (char)(x+65);
    }
};

int main(){
    int n;
    char x, y, z;

    cin >> n;
    Tree T(n);
    for(int i=0; i<n; i++){
        cin >> x >> y >> z;
        T.add_sub_tree(x-65,y-65,z-65);
    }

    T.preorder(0);
    cout << endl;
    T.inorder(0);
    cout << endl;
    T.postorder(0);

    return 0;
}
