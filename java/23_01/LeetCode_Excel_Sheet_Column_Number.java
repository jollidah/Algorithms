class Solution {
    public int titleToNumber(String columnTitle) {
        int res = 0;
        for(int cnt = 0, i = columnTitle.length() - 1; i >= 0; i--, cnt++){
            res += (columnTitle.charAt(i) - 'A' + 1) * Math.pow(26, cnt);
        }
        return res;
    }
}

// https://leetcode.com/problems/excel-sheet-column-number/description/
