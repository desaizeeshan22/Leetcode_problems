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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length=0;
        ListNode curr=head;
        while(curr!=null){
            curr=curr.next;
            length++;
        }
        curr=head;
        if(length==n||length==1){
            head=head.next;        
            return head;
        }
        int i=0;
        while(i<(length-n)-1){
            curr=curr.next;
            i+=1;
        }
        curr.next=curr.next.next;
        return head;
        
    }
}