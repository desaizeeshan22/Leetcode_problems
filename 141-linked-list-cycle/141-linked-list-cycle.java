/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
       ListNode lagging=head;
       ListNode leading=head;
       while(leading!=null&&leading.next !=null){
           leading=leading.next.next;
           lagging=lagging.next;
           if(leading==lagging){
               return true;
           }
       }
        return false;
    }
}