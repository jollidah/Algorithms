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
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {   # A 리스트와 B 리스트를 서로 더한 후 하나씩 비교하면 O(n + m) 복잡도 가능
       ListNode a = headA;
       ListNode b = headB;
       while (a != b && (a != null || b != null))   # intersection이 없는 경우도 고려해야 한다 그렇기 때문에 a 와 b 둘다 null일 땐 while문을 종료한다.
       {
           a = (a == null)? headB : a.next;
           b = (b == null)? headA : b.next;
       }
       return a;
    }
}

# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
