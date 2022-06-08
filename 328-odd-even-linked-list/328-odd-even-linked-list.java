/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        
        int index=0;
        ListNode oddHead=null;
        ListNode evenHead=null;
        ListNode oddTail=null;
        ListNode evenTail=null;
        ListNode curr=head;
        while(curr!=null){
            if(index%2==0){
                if(evenHead==null){
                    evenHead=curr;
                    evenTail=curr;
                }
                else{
                    evenTail.next=curr;
                    evenTail=curr;
                }
            }
            else{
                 if(oddHead==null){
                    oddHead=curr;
                    oddTail=curr;
                }
                else{
                    oddTail.next=curr;
                    oddTail=curr;
                }
            }
            curr=curr.next;
            index+=1;
        }
        if(oddHead==null||evenHead==null){
            return head;
        }
        evenTail.next=oddHead;
        oddTail.next=null;
        return evenHead;
    }
}