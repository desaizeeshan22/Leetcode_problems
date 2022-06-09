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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode ptr1=head;
        ListNode ptr2=head;
        int length=this.length(head);
        for(int i=0;i<k-1;i++){
            ptr1=ptr1.next;
        }
        for(int i=0;i<length-k;i++){
            ptr2=ptr2.next;
        }
        int temp=ptr1.val;
        ptr1.val=ptr2.val;
        ptr2.val=temp;
        return head;
    }
    public int length(ListNode head){
        int length=0;
        while(head!=null){
            length+=1;
            head=head.next;
        }
        return length;
    }
}