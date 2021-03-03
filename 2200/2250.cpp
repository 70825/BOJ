#include <bits/stdc++.h>
using namespace std;

class Tree{
private:
    int N, pos=1;
    vector<int> parent;
    vector<int> lc;
    vector<int> rc;
    vector<int> level;
    vector<int> position;
public:
    int root;
    
    Tree():N(0){}
    Tree(int n):N(n){
        parent.resize(n,-1);
        lc.resize(n,-2);
        rc.resize(n,-2);
        level.resize(n,0);
        position.resize(n,-1);
    }
    void connect_node(int x, int y, int z){
        if(y!=-2){
            lc[x] = y;
            parent[y] = x;
        }
        if(z!=-2){
            rc[x] = z;
            parent[z] = x;
        }
    }
    void find_root(int x){
        if(parent[x] == -1) root = x;
        else find_root(parent[x]);
    }
    void set_level(){
        queue<int> q;
        q.push(root);
        level[root] = 1;
        while(!q.empty()){
            int x = q.front(); q.pop();
            if(lc[x]!=-2){
                level[lc[x]] = level[x]+1;
                q.push(lc[x]);
            }
            if(rc[x]!=-2){
                level[rc[x]] = level[x]+1;
                q.push(rc[x]);
            }
        }
    }
    void set_pos(int x){
        if(lc[x]!=-2) set_pos(lc[x]);
        position[x] = pos; pos+=1;
        if(rc[x]!=-2) set_pos(rc[x]);
    }
    void find_max(){
        queue<int> nq;
        nq.push(root);
        int max_lv = 1, max_dia[2] = {0,0}, lv=2;
        while(1){
            queue<int> q;
            int dia[2] = {10001,-1};
            while(!nq.empty()) {
                int x = nq.front();nq.pop();
                for (auto nx: {lc[x], rc[x]}) {
                    if (nx != -2) {
                        if (position[nx] < dia[0]) dia[0] = position[nx];
                        else if (position[nx] > dia[1]) dia[1] = position[nx];
                        q.push(nx);
                    }
                }
            }
            if (dia[1] - dia[0] > max_dia[1] - max_dia[0]) {
                max_dia[0] = dia[0];
                max_dia[1] = dia[1];
                max_lv = lv;
            }
            if(q.empty()) break;
            nq = q;
            lv+=1;
        }
        cout << max_lv << " " << max_dia[1] - max_dia[0] + 1;
    }
};

int main(){
    int n,x,y,z;
    cin >> n;

    Tree T(n);
    for(int i=0; i<n; i++){
        cin >> x >> y >> z;
        T.connect_node(x-1,y-1,z-1);
    }
    T.find_root(0);
    
    T.set_level();
    T.set_pos(T.root);
    
    T.find_max();

}