class Solution {
    public int maxSubArray(int[] nums) {
        int curSum = nums[0];
        int maxValue = nums[0];
        for (int i = 1; i < nums.length; i++)
        {
            if (0 < curSum)
            {
                curSum += nums[i];
            }
            else
            {
                curSum = nums[i];
            }
            maxValue = Math.max(curSum, maxValue);
        }
        return maxValue;
    }
}

# https://leetcode.com/problems/maximum-subarray/description/
