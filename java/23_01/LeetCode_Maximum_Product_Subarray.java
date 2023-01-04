class Solution {
    public int maxProduct(int[] nums) {
        int maxCurV = nums[0];
        int minCurV = nums[0];
        int maxV = nums[0];
        int minV = nums[0];
        for(int i = 1; i < nums.length; i++)    # 최소값과 최댓값을 모두 구하여 음수도 포함
        {
            int maxTmp = maxCurV;
            int minTmp = minCurV;
            maxCurV = Math.max(nums[i], minCurV * nums[i]);
            maxCurV = Math.max(maxCurV, maxTmp * nums[i]);
            maxV = Math.max(maxCurV, maxV);
            minCurV = Math.min(nums[i], maxTmp * nums[i]);
            minCurV = Math.min(minCurV, minTmp * nums[i]);
            minV = Math.min(minCurV, minV);
            System.out.printf("%d   %d\n", maxV, minV);
        }
        return maxV;
    }
}

#  https://leetcode.com/problems/maximum-product-subarray/description/
