#include <bits/stdc++.h>
using namespace std;
typedef long double db;

db in(db x1,db y1, db x2, db y2){
    return x1*x2+y1*y2;
}
db out(db x1,db y1, db x2, db y2){
    return x1*y2-x2*y1;
}
db dist(db x1,db y1, db x2, db y2){
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2));
}
db height(db x1, db y1, db x2, db y2, db x3, db y3){
    db in1=in(x2-x1,y2-y1,x3-x1,y3-y1);
    db in2=in(x1-x2,y1-y2,x3-x2,y3-y2);
    if(in1*in2>=0) {
        return abs(out(x2 - x1, y2 - y1, x3 - x1, y3 - y1)) / dist(x1, y1, x2, y2);
    }
    return -1;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M;
    cin >> N >> M;
    vector<db> yx,yy;
    db res = -1;
    for(int i=0; i<N; i++){
        db x1,y1,x2,y2;
        cin >> x1 >> y1 >> x2 >> y2;
        yx.push_back(x1);
        yx.push_back(x2);
        yy.push_back(y1);
        yy.push_back(y2);
    }
    for(int i=0; i<M;i++){
        db x1,y1,x2,y2,x3,y3,x4,y4,temp;
        cin >> x3 >> y3 >> x4 >> y4;
        for(int j=0;j<N;j++){
            x1=yx[2*j];y1=yy[2*j];
            x2=yx[2*j+1];y2=yy[2*j+1];
            db D = dist(x1,y1,x3,y3);
            D=min(D,dist(x1,y1,x4,y4));
            D=min(D,dist(x2,y2,x3,y3));
            D=min(D,dist(x2,y2,x4,y4));
            temp=height(x1,y1,x2,y2,x3,y3);
            if(temp>=0) D=min(D,temp);
            temp=height(x1,y1,x2,y2,x4,y4);
            if(temp>=0) D=min(D,temp);
            temp=height(x3,y3,x4,y4,x1,y1);
            if(temp>=0) D=min(D,temp);
            temp=height(x3,y3,x4,y4,x2,y2);
            if(temp>=0) D=min(D,temp);
            if(res==-1)res=D;
            else res=min(res,D);
        }
    }
    cout.precision(10);
    cout << res << "\n";
}