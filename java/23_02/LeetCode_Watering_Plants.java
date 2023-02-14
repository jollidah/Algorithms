// Watering Plants

class Solution {
    public int wateringPlants(int[] plants, int capacity) {
        int cnt = 0, curWater = capacity, target = 0;
        while (target < plants.length) {
            if (curWater >= plants[target]) {
                curWater -= plants[target++];
                cnt++;
            }
            else{
                cnt += (2 * target);
                curWater = capacity;
            }
        }
        return cnt;
    }
}

// https://leetcode.com/problems/watering-plants/description/
