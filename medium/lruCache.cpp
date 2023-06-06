struct Node {
    int key;
    int val;
    Node *next;
    Node *prev;
    Node(int key, int val) : key(key), val(val), next(nullptr), prev(nullptr) {}
};

class LRUCache {
    int cap;
    unordered_map<int, Node*> dic;
    Node *head = new Node(-1, -1), *tail = new Node(-1, -1);
public:
    LRUCache(int capacity) {
        this->cap = capacity;
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (dic.find(key) == dic.end()) return -1;
        
        Node *node = dic[key];
        remove(node);
        add(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (dic.find(key) != dic.end()) {
            Node *old = dic[key];
            remove(old);
        }
        
        Node * node = new Node(key, value);
        dic[key] = node;
        add(node);
        
        if (dic.size() > cap) {
            Node *toDel = head->next;
            remove(toDel);
            dic.erase(toDel->key);
        }
    }
    
    void add(Node *node) {
        Node *previousEnd = tail->prev;
        previousEnd->next = node;
        node->prev = previousEnd;
        node->next = tail;
        tail->prev = node;
    }
    
    void remove(Node *node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */