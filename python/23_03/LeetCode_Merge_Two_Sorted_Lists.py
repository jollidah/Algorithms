# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        head=ListNode(-1)
        cursor=head
        
        while l1!=None and l2!=None:
            if l1.val <= l2.val:
                cursor.next=l1 # Update next node
                l1=l1.next # Update l1
            else:
                cursor.next=l2 #Update next node
                l2=l2.next # Updata l2
            
            cursor=cursor.next #Move cursor
        
        
        # Last node  
        if l1!=None:
            cursor.next=l1
        
        else:
            cursor.next=l2
            
        return head.next
