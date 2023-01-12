class Solution {
    public int findPeakElement(int[] nums) {
        int lp = 0;
        int rp = nums.length - 1;
        int mid;
        while(lp < rp){
            mid = (lp + rp) / 2;
            if (nums[mid] < nums[mid + 1])
            {
                lp = mid + 1;
            }
            else
            {
                rp = mid;
            }
        }
        return lp;
    }
}

# https://leetcode.com/problems/find-peak-element/description/
