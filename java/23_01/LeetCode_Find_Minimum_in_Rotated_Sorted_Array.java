class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int lp = 0;
        int rp = n - 1;
        int mid;
        while(lp < rp)
        {
            mid = (lp + rp) / 2;
            if(nums[mid] < nums[rp]){
                rp = mid;
            }
            else {
                lp = mid + 1;
            }
        }
        return nums[lp];
    }
}

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
