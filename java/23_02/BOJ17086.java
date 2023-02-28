// 아기 상어2

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        try {
            int n, m, maxV;
            int [] tmp;
            int [] dx = new int[]{0, 1, 1, 1, 0, -1, -1, -1};
            int [] dy = new int[]{1, 1, 0, -1, -1, -1, 0, 1};
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            Queue <int []> q = new LinkedList<>();
            int[][] dp;
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            dp = new int [n][m];
            for(int i = 0; i < n; i++){
                Arrays.fill(dp[i], Integer.MAX_VALUE);
            }

            for(int i = 0; i < n; i++){
                st = new StringTokenizer(br.readLine());
                for(int j = 0; j < m; j++){
                    if(st.nextToken().equals("1")){
                        dp[i][j] = 0;
                        q.add(new int []{i, j});
                    }
                }
            }
            maxV = 0;
            while(!q.isEmpty()){
                tmp = q.poll();
                for(int i = 0; i < 8; i ++){
                    maxV = Math.max(maxV, dp[tmp[0]][tmp[1]]);
                    int tmpY = tmp[0] + dy[i];
                    int tmpX = tmp[1] + dx[i];
                    if((tmpY >= 0 && tmpY < n) && (tmpX >= 0 && tmpX < m)){
                        if(dp[tmpY][tmpX] > dp[tmp[0]][tmp[1]] + 1){
                            dp[tmpY][tmpX] = dp[tmp[0]][tmp[1]] + 1;
                            q.add(new int[] {tmpY, tmpX});
                        }
                    }
                }
            }
            System.out.println(maxV);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/17086
