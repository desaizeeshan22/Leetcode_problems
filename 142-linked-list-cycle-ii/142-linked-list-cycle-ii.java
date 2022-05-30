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
    public ListNode detectCycle(ListNode head) {
        Map<ListNode,Integer>hashTable=new HashMap<ListNode,Integer>();
        int count=0;
        ListNode curr=head;
        while(curr!=null){
            if(hashTable.containsKey(curr)){
                return curr;
            }
            hashTable.put(curr,count);
            count+=1;
            curr=curr.next;
        }
        return null;
    }
}