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
     public ListNode reverseLinkedList(ListNode head, int k) {
         ListNode curr=head;
         ListNode prev=null;
         while(curr!=null&&k>0){
             ListNode next=curr.next;
             curr.next=prev;
             prev=curr;
             curr=next;
             k--;
         }
         return prev;
     }
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode ptr=head;
        ListNode prevFirst=null;
        ListNode newHead=null;
        while(ptr!=null){
            ptr=head;
            int count=0;
            while(ptr!=null&&count<k){
                ptr=ptr.next;
                count+=1;
            }
            if(count==k){
                ListNode revHead=this.reverseLinkedList(head,k);
            if(newHead==null){newHead=revHead;}
            if(prevFirst!=null){prevFirst.next=revHead;}
            prevFirst=head;
            head=ptr;
                }
        }
        if(prevFirst!=null){
            prevFirst.next=head;
        }
        return newHead ==null ? head:newHead;
    }
}