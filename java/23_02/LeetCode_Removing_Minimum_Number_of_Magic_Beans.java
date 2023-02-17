// Removing Minimum Number of Magic Beans

import java.util.*;
class Solution {

    public long minimumRemoval(int[] beans) {
        long res, sum = 0;
        Arrays.sort(beans);
        for (int tmp : beans) {
            sum += tmp;
        }
        res = sum;
        System.out.println(sum);
        for (int i = 0; i < beans.length; i++) {
            res = Math.min(sum - ((long) (beans.length - i) * beans[i]), res);
        }
        return res;
    }
}

// https://leetcode.com/problems/removing-minimum-number-of-magic-beans/description/
