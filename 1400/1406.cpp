#include <bits/stdc++.h>
using namespace std;

class Node{
    friend class circular_doubly_linked_list;
private:
    char value;
    Node *next;
    Node *prev;
public:
    Node(char v, Node *n, Node *p):value(v),next(n),prev(p){}
};

class circular_doubly_linked_list{
private:
    Node *head;
    Node *cursor;
public:
    circular_doubly_linked_list(){
        head = nullptr;
        cursor = nullptr; //현재 커서의 위치
        push_back('$'); //head는 무조건 $
    }
    void push_back(char v){
        Node *new_node = new Node(v,nullptr,nullptr);
        if(head == nullptr){
            head = new_node;
            head -> next = head -> prev = head;
            cursor = head;
        }
        else{
            new_node -> prev = head -> prev;
            new_node -> next = head;
            head -> prev -> next = new_node;
            head -> prev = new_node;
            cursor = new_node;
        }
    }
    void move(char v){
        if(cursor != head && v == 'L')
            cursor = cursor -> prev;
        else if(cursor != head->prev && v == 'D')
            cursor = cursor -> next;
    }
    void insert(char v){
        Node *new_node = new Node(v,nullptr,nullptr);

        new_node -> prev = cursor;
        new_node -> next = cursor -> next;
        cursor -> next -> prev = new_node;
        cursor -> next = new_node;

        cursor = new_node;
    }

    void erase(){
        if(cursor != head){
            cursor -> prev -> next = cursor -> next;
            cursor -> next -> prev = cursor -> prev;
            cursor = cursor -> prev;
        }
    }

    void print(){
        Node *now = head;
        while(now -> next != head){
            now = now -> next;
            cout << now -> value;
        }
        cout << endl;
    }
};

int main(){
    string x;
    int n;
    char y;
    circular_doubly_linked_list CDLL;

    cin >> x;
    for(int i=0; i<x.size(); i++)
        CDLL.push_back(x[i]);

    cin >> n;
    for(int i=0; i<n; i++){
        cin >> y;
        if(y == 'L' || y == 'D') CDLL.move(y);
        else if(y == 'B') CDLL.erase();
        else{
            cin >> y;
            CDLL.insert(y);
        }
    }

    CDLL.print();

    return 0;
}