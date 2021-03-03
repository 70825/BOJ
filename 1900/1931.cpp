#include <bits/stdc++.h>
using namespace std;

int n,Time=0,ans=0;

struct D{
    int start;
    int end;
};

bool sorted(D a,D b){
    if(a.end==b.end)
        return a.start < b.start;
    else
        return a.end < b.end;
}

int main(){
    cin >> n;
    vector<D> t(n);
    for (int i = 0; i < n; i++){
        cin >> t[i].start >> t[i].end;
    }
    sort(t.begin(), t.end(), sorted);
    for(int i = 0; i < n; i++){
        if(Time<=t[i].start){
            ans+=1;
            Time=t[i].end;
        }
    }
    cout << ans << endl;
}