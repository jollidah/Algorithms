class Solution {
    public int compareVersion(String version1, String version2) {
        String[] v1_list = version1.split("\\.");
        String[] v2_list = version2.split("\\.");
        System.out.println(v1_list[1]);
        System.out.println(v2_list[1]);
        int ptr1 = 0, ptr2 = 0;
        int i1, i2;
        while (ptr1 < v1_list.length && ptr2 < v2_list.length) {    // 탈출 조건이 전문에서 끄나면 ptr2가 더해지지 못함

            i1 = Integer.parseInt(v1_list[ptr1++]);
            i2 = Integer.parseInt(v2_list[ptr2++]);
            System.out.println(i1);
            System.out.println(i2);
            if (i1 < i2)
            {
                return -1;
            }
            else if(i1 > i2){
                return 1;
            }
        }
        while (ptr1 < v1_list.length)
        {
            if (Integer.parseInt(v1_list[ptr1]) != 0){
                return 1;
            }
            ptr1++;
        }
        while (ptr2 < v2_list.length)
        {
            if (Integer.parseInt(v2_list[ptr2]) != 0){
                return -1;
            }
            ptr2++;
        }
        return 0;
    }
}

# https://leetcode.com/problems/compare-version-numbers/description/
