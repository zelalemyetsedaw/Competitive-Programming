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
    ListNode* deleteDuplicates(ListNode* head) {
       if(head==NULL || head->next == NULL)
       {
           return head;
       }
        ListNode* temp = new ListNode();
        temp->next = head;
        
        ListNode* itr = temp;
        while(itr->next && itr->next->next)
        {
            if(itr->next->val== itr->next->next->val)
            {
                int variable = itr->next->val;
                while(itr->next != NULL && itr->next->val == variable)
                {
                    itr->next = itr->next->next;
                }
            }
            else itr = itr->next;
        }
        return temp->next;
    }
};
