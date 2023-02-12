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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* current = NULL;
        ListNode* temp = head;
        ListNode* next = NULL;
        while(temp!= NULL)
        {
            
            current = temp;
            next = temp->next;
            current->next = prev;
            prev = temp;
            temp = next;
        }
    
        return current;
    }
};