// Search Insert Position

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
    let mut lp = 0;
    let mut rp = nums.len() - 1;
    if target <= nums[lp]{
        return 0
    }
    if target > nums[rp]{
        return (rp + 1)  as i32
    }
    while lp < rp{
        let mid = (lp + rp) / 2;
        if nums[mid] < target{
            lp = mid + 1;
        } else{
            rp = mid;
        }
    }
    return rp as i32
    }
}

// https://leetcode.com/problems/search-insert-position/description/
