# Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pos = head
        cnt = 1
        if head == None:
            return head
        if k == 0:
            return head
        while pos.next != None:
            cnt += 1
            pos = pos.next
        pos.next = head
        l = cnt
        k %= l
        pos = head
        for _ in range(l - 1 - k):
            pos = pos.next
        head = pos.next
        pos.next = None
        return head

# https://leetcode.com/problems/rotate-list/description/
