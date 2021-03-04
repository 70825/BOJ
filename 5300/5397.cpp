#include <bits/stdc++.h>
using namespace std;

class Node{
    friend class circular_doubly_linked_list;
private:
    char value;
    Node *next;
    Node *prev;
public:
    Node(char v, Node *n, Node *p):value(v),next(n),prev(p){};
};

class circular_doubly_linked_list{
private:
    Node *head;
    Node *cursor;
public:
    circular_doubly_linked_list(){
        Node *new_node = new Node('$',nullptr,nullptr);
        head = cursor = new_node;
        head -> next = head -> prev = new_node;
    }
    void move(char z){
        if(z == '<' && cursor != head)
            cursor = cursor -> prev;
        else if(z == '>' && cursor != head -> prev)
            cursor = cursor -> next;
    }
    void insert(char v){
        Node *new_node = new Node(v, cursor->next, cursor);
        cursor -> next -> prev = new_node;
        cursor -> next = new_node;
        cursor = new_node;
        }

    void erase(){
        Node *tmp = cursor -> prev;
        if(cursor != head) {
            cursor->prev->next = cursor->next;
            cursor->next->prev = cursor->prev;

            delete cursor;
            cursor = tmp;
        }
    }

    void print(){
        Node *dest = head;
        while(dest -> next != head){
            dest = dest -> next;
            cout << dest -> value;
        }
        cout << endl;
    }
};

int main(){
    int t;
    cin >> t;

    for(int i=0; i<t; i++){
        string x;
        circular_doubly_linked_list CDLL;

        cin >> x;
        for(int j=0; j<x.size(); j++){
            if(x[j] == '<' || x[j] == '>') CDLL.move(x[j]);
            else if(x[j] == '-') CDLL.erase();
            else CDLL.insert(x[j]);
        }

        CDLL.print();
    }
}