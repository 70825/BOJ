#include <bits/stdc++.h>
using namespace std;

class Node{
    friend class circular_doubly_linked_list;
private:
    int value;
    int num;
    Node* next;
    Node* prev;
public:
    Node(int v, int t, Node* n, Node* p):value(v),num(t),next(n),prev(p){}
};

class circular_doubly_linked_list{
private:
    Node* head;
public:
    circular_doubly_linked_list(){
        head = nullptr;
    }
    void push_back(int v, int t){
        Node* new_node = new Node(v, t, nullptr, nullptr);
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
    }

    void erase(){
        int ans = head->value;

        cout << head -> num << " ";
        head -> prev -> next = head -> next;
        head -> next -> prev = head -> prev;

        Node* next_node = head;
        if(ans<0)
            for(int i=0; i<ans*(-1); i++)
                next_node = next_node -> prev;
        else
            for(int i=0; i<ans; i++)
                next_node = next_node -> next;

        delete head;
        head = next_node;
    }

};

int main(){
    int n,A[1001];

    cin >> n;
    for(int i=0; i<n; i++) cin >> A[i];

    circular_doubly_linked_list CDLL;
    for(int i=0; i<n; i++) CDLL.push_back(A[i],i+1);

    for(int i=0; i<n; i++) CDLL.erase();

    return 0;
}