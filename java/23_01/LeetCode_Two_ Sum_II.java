class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int [] res = new int[2];
        int lp = 0;
        int rp = 1;
        int sum = 0;
        while(numbers[lp] + numbers[lp + 1] < target)
        {
            lp++;
        }
        rp = lp + 1;
        while((sum = numbers[lp] + numbers[rp]) != target){
            if (sum < target)
            {
                rp++;
            }
            else
            {
                lp--;
            }
        }
        res[0] = lp + 1;
        res[1] = rp + 1;
        return res;
    }
}

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
