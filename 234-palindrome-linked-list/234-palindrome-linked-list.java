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
    public boolean isPalindrome(ListNode head) {
        Deque<Integer> st=new ArrayDeque<Integer>();
        ListNode first=head;
        while(first!=null){
            st.push(first.val);
            first=first.next;
        }
        first=head;
        while(!st.isEmpty()&&first.next!=null){
            int stVal=st.pop();
            int llVal=first.val;
            if(stVal!=llVal){
                return false;
            }
            first=first.next;
        }
        return true;
    }
    public ListNode reverse(ListNode head){
        ListNode curr=head;
        ListNode prev=null;
        while(curr!=null){
            ListNode next=curr.next;
            curr.next=prev;
            prev=curr;
            curr=next;
        }
        return prev;
    }
}