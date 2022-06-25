class Solution:
    def findMedianSortedArrays(self , nums1, nums2) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        cnt = 0
        res = 0
        while nums1 and nums2 and cnt < int((l1 + l2 -1) / 2):
            if nums1[0] <= nums2[0]:
                nums1.pop(0)
                cnt += 1
            else:
                nums2.pop(0)
                cnt += 1
        if nums1:
            while cnt < int((l1 + l2 -1) / 2):
                nums1.pop(0)
                cnt += 1
        else:
            while cnt < int((l1 + l2 - 1) / 2):
                nums2.pop(0)
                cnt += 1
        if (l1 + l2) % 2 == 0:
            for i in range(2):
                if nums1 and nums2:
                    if nums1[0] < nums2[0]:
                        res += nums1.pop(0)
                    else:
                        res += nums2.pop(0)
                elif nums1:
                    res += nums1.pop(0)
                else:
                    res += nums2.pop(0)
            return res / 2
        else:
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    return nums1[0]
                else:
                    return nums2[0]
            elif nums1:
                return nums1[0]
            else:
                return nums2[0]
              
       # https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
