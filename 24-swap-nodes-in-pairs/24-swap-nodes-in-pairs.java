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
    public ListNode swapPairs(ListNode head) {
        ListNode curr=head;
        ListNode prevFirst=null;
        boolean firstPass=true;
        while(curr!=null){
               int k=2;
               ListNode currHead=curr;
               ListNode prev=null;
               while(curr!=null&&k>0){
                   ListNode temp=curr.next;
                   curr.next=prev;
                   prev=curr;
                   curr=temp;
                   k--;
               }
            if(firstPass){head=prev;firstPass=false;}
            else{prevFirst.next=prev;}
            prevFirst=currHead;
        }
     return head;
    }
}