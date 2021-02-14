#include <bits/stdc++.h>
using namespace std;

class Node{
    friend class circular_linked_list;
private:
    int value;
    Node *next;
public:
    Node(int v,Node *n):value(v),next(n){}
};
class circular_linked_list{
private:
    Node *tail;
public:
    circular_linked_list(){
        tail = nullptr;
    }
    void push_back(int k){
        Node *new_node = new Node(k,nullptr);
        if(tail==nullptr){
            tail = new_node;
            tail -> next = new_node;
        }
        else{
            new_node -> next = tail -> next;
            tail -> next = new_node;
            tail = new_node;
        }
    }
    void erase(int k, int z){
        Node *dest = tail;
        for(int i=0; i<k; i++){
            if(i==k-1) tail = dest;
            dest = dest -> next;
        }

        if(z==0)
            cout << dest -> value;
        else
            cout  << ", " << dest -> value;

        tail -> next = dest -> next;
        delete dest;
    }
};

int main(){
    int n, k;
    cin >> n >> k;

    circular_linked_list CLL;

    for(int i=0; i<n; i++) CLL.push_back(i+1);

    cout << "<";
    for(int i=0; i<n; i++) CLL.erase(k, i);
    cout << ">";
}