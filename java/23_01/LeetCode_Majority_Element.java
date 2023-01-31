import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {
        int target = nums.length / 2;
        int cnt = 0, res = nums[0];
        Arrays.sort(nums);
        for(int i = 0; i < nums.length - 1; i++){
            if(nums[i] == nums[i + 1]){
                if(++cnt == target){
                    res = nums[i];
                    break;
                }
            }
            else{
                cnt = 0;
            }
        }
        return res;
    }
}

// https://leetcode.com/problems/majority-element/description/
