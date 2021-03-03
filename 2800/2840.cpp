#include <bits/stdc++.h>
using namespace std;

int alphabet[27] = {0};
bool err = false;

class Node{
    friend class circular_doubly_linked_list;
private:
    char value = '.';
    Node *next;
    Node *prev;
public:
    Node(char v, Node *n, Node *p)
    {
        value = v;
        next = n;
        prev = p;
    }
};

class circular_doubly_linked_list{
private:
    Node *head;
public:
    circular_doubly_linked_list(){
        head = nullptr;
    }
    void push_back(char x){
        Node *new_node = new Node(x, nullptr,nullptr);
        if(head == nullptr){
            head = new_node;
            head -> next = head;
            head -> prev = head;
        }
        else{
            new_node -> next = head;
            new_node -> prev = head -> prev;
            head -> prev -> next = new_node;
            head -> prev = new_node;
        }
    }
    void input(int k, char z){
        Node *dest = head;
        for(int i=0; i<k; i++) dest = dest -> prev;
        head = dest;

        if(head -> value == '.'){
            head -> value = z;
            alphabet[z-65] += 1;
            if(alphabet[z-65] > 1) err = true;
        }
        else if(head -> value != z) err = true;
    }

    void print(int k){
        Node *dest = head;
        for(int i=0; i<k; i++){
            if(dest -> value == '.')
                cout << "?";
            else
                cout << dest -> value;
            dest = dest -> next;
        }
    }
};

int main(){
    int n,k,a;
    char b;
    cin >> n >> k;

    circular_doubly_linked_list CDLL;
    for(int i=0; i<n; i++) CDLL.push_back('.');


    for(int i=0; i<k; i++){
        cin >> a >> b;
        CDLL.input(a,b);
    }

    if(err == true) cout << "!";
    else CDLL.print(n);

    return 0;
}
