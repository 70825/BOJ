#include <bits/stdc++.h>
using namespace std;

class Tree{
public:
    int N;
    vector<int> visited;
    int arr[500][500] = {0};

    Tree():N(0){}
    Tree(int n):N(n){
        visited.resize(N,0);
    }
    void connect_node(int x, int y){
        arr[x][y] = 1;
        arr[y][x] = 1;
    }
    int find_tree(int a){
        queue<int> q;
        q.push(a);
        visited[a] = 1;
        while(!q.empty()){
            int x = q.front(); q.pop();
            for(int i=0; i<N; i++){
                if(arr[x][i]){
                    if(visited[i] > 0) return 0;
                    arr[x][i] = 0; arr[i][x] = 0;
                    q.push(i);
                    visited[i] = 1;
                }
            }
        }
        return 1;
    }
};

int main(){
    int n,m,a,b,z=1;
    while(1) {
        cin >> n >> m;
        if(n==0 && m==0) break;

        Tree T(n);
        for(int i=0; i<m; i++){
            cin >> a >> b;
            T.connect_node(a-1,b-1);
        }
        int ans = 0;
        for(int i=0; i<n; i++){
            if(!T.visited[i]) ans+=T.find_tree(i);
        }

        cout << "Case " << z <<": ";
        if(ans==0) cout << "No trees.";
        else if(ans==1) cout << "There is one tree.";
        else cout << "A forest of " << ans << " trees.";
        cout << endl;
        z++;
    }
}