class Solution {
    public String convertToTitle(int columnNumber) {
        String res = "";
        columnNumber -= 1;
        while (columnNumber > 25){
            res = (char) ('A' + columnNumber % 26) + res;
            columnNumber = columnNumber / 26 - 1;
        }
        res = (char) ('A' + columnNumber) + res;        
        return res;
    }
}

// https://leetcode.com/problems/excel-sheet-column-title/description/
