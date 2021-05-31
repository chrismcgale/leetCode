/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
 
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* sol = new ListNode();
        ListNode* curr = sol;
        int carry = 0;
        while (l1 || l2) {
            int sum = carry;
            if(l1) sum += l1->val;
            if(l2) sum += l2->val;
            
            if(sum >= 10) {
                sum %= 10;
                carry = 1;
            } else carry = 0;
            
            curr->val = sum;
            
            if(l1) l1 = l1->next;
            if(l2) l2 = l2->next;
            
            if (l1 || l2 || carry == 1) curr->next = new ListNode();
            curr = curr->next;
        }
        
        if (carry == 1) {
            curr->val = 1;
        }
        
        return sol;
    }
};
