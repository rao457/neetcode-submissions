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
    public ListNode removeNthFromEnd(ListNode head, int num) {
        if (head == null) return null;
        int counter = 0;
        ListNode currNode = head;
        while(currNode != null) {
            currNode = currNode.next;
            counter++;
        }
        if (num == counter) {
            return head.next;
        }
        currNode = head;
        for (int i = 1; i < counter-num; i++) {
            currNode = currNode.next;
        }
        if (currNode.next != null) {
            currNode.next = currNode.next.next;
        }
        return head;
    }}
