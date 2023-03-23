# Merge k Sorted Lists

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = PriorityQueue()
        res = None
        for i in range(len(lists)):
            if lists[i]:
                pq.put([lists[i].val, i])
        if not pq.empty():
            idx = pq.get()[1]
            print(idx)
            res = lists[idx]
            if res.next:
                lists[idx] = lists[idx].next
                pq.put([res.next.val, idx])
        pos = res
        while not pq.empty():
            idx = pq.get()[1]
            pos.next = lists[idx]
            pos = lists[idx]
            if pos.next:
                lists[idx] = lists[idx].next
                pq.put([pos.next.val, idx])
        return res

# https://leetcode.com/problems/merge-k-sorted-lists/description/
