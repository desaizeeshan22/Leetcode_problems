/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode*lagging=head;
        ListNode*leading=head;
        while(leading!=NULL&&leading->next!=NULL){
            leading=leading->next->next;
            lagging=lagging->next;
            if(lagging==leading){
                return true;
            }
        }
        return false;
    }
};