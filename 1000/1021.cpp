#include <bits/stdc++.h>
using namespace std;

class Node{
    friend class circular_doubly_linked_list;
private:
    int value;
    Node* next;
    Node* prev;
public:
    Node(int v, Node* n, Node* p):value(v),next(n),prev(p){}
};

class circular_doubly_linked_list{
private:
    Node* head;
    int size = 0;
public:
    circular_doubly_linked_list(){
        size = 0;
        head = nullptr;
    }
    void push_back(int v){
        Node* new_node = new Node(v, nullptr, nullptr);
        if(head == nullptr){
            head = new_node;
            new_node -> next = new_node;
            new_node -> prev = new_node;
        }
        else{
            new_node -> prev = head -> prev;
            new_node -> next = head;
            head -> prev -> next = new_node;
            head -> prev = new_node;
        }
        size++;
    }

    void erase(int v){
        Node* dest = head;
        while(dest -> value != v){
            dest = dest -> next;
        }
        dest -> prev -> next = dest -> next;
        dest -> next -> prev = dest -> prev;
        head = dest -> next;
        delete dest;
        size--;
    }

    int find(int target, int k){//k==1 오른쪽으로 회전, k==0 왼쪽으로 회전
        Node* dest = head;
        if (dest -> value == target) return 0;
        int z = 0;
        if(k==1)
            do{
                z++;
                dest = dest -> next;
                if(dest->value == target) return z;
            }while(dest != head);
        else
            do{
                z++;
                dest = dest -> prev;
                if(dest->value == target) return z;
            }while(dest != head);
    }

    void print(){
        cout << "[ ";
        Node *dest = head;
        for(int i=0; i<size; i++){
            cout << dest -> value << " ";
            dest = dest -> next;
        }
        cout << "]" << endl;
    }
};

int main(){
    int n,m,A[51],ans=0;

    cin >> n >> m;
    for(int i=0; i<m; i++) cin >> A[i];

    circular_doubly_linked_list CDLL;
    for(int i=0; i<n; i++) CDLL.push_back(i+1);

    for(int i=0; i<m; i++){
        ans += min(CDLL.find(A[i],1),CDLL.find(A[i],0));
        CDLL.erase(A[i]);
    }

    cout << ans << endl;

    return 0;
}