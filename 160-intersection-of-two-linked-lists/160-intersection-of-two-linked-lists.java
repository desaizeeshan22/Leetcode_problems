/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lengthA=this.lengthLinkedList(headA);
        int lengthB=this.lengthLinkedList(headB);
        ListNode curr2=null;
        ListNode curr=null;
        if(lengthA>lengthB){
            int diff=lengthA-lengthB;
            curr=headA;
            for(int i=0;i<diff;i++){
                curr=curr.next;
            }
            curr2=headB;
        }
        else{
            int diff=lengthB-lengthA;
            curr=headB;
             for(int i=0;i<diff;i++){
                curr=curr.next;
            }
            curr2=headA;  
        }
        while(curr2!=null || curr!=null){
                if(curr==curr2){
                    return curr;
                }
                curr=curr.next;
                curr2=curr2.next;
            }
        return null;
    }
    public int lengthLinkedList(ListNode head){
        int length=0;
        while(head!=null){
            length+=1;
            head=head.next;
        }
        return length;
    }
}