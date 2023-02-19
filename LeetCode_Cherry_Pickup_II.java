// Cherry Pickup II

import java.util.Arrays;

class Solution {

    int h;
    int w;

    int[] dx = new int[]{- 1, 0, 1};

    int[][][]dp;


    public int dfs(int[][] g, int lp, int rp,int cherry, int cnt) {
        if (cnt == h) {
            return cherry;
        } else{
            cherry += g[cnt][lp] + g[cnt][rp];
            if (dp[cnt][lp][rp] != -1) {
                return dp[cnt][lp][rp] + cherry ;
            }
            cnt++;
            int maxV = 0;
            for (int i = 0; i < 3; i++) {
                int tmpL = lp + dx[i];
                if (tmpL >= 0 && tmpL < w - 1) {
                    for (int j = 0; j < 3; j++) {
                        int tmpR = rp + dx[j];
                        if (tmpR > tmpL && tmpR < w) {
                            maxV = Math.max(maxV, dfs(g, tmpL, tmpR, cherry, cnt));
                        }
                    }
                }
            }
            dp[cnt - 1][lp][rp] = maxV - cherry;
            return maxV;
        }
    }

    public int cherryPickup(int[][] grid) {
        h =  grid.length;
        w = grid[0].length;
        dp = new int[h][w][w];
        for (int[][] arr1 : dp) {
            for (int[] arr2 : arr1) {
                Arrays.fill(arr2, -1);
            }
        }
        int res = dfs(grid, 0, w - 1, 0, 0);
        System.out.println(res);
        return res;
    }
}

// https://leetcode.com/problems/cherry-pickup-ii/description/?envType=study-plan&id=dynamic-programming-iii
