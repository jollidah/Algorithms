// 직사각형으로 

import java.util.*;
import java.io.*;

public class Main {

    static int[][] grid;
    static long calcSum(int y1, int x1, int y2, int x2){
        long sum = 0;
        for(int i = y1; i <= y2; i++){
            for(int j = x1; j <= x2; j++){
                sum += grid[i][j];
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        try {
            int n, m;
            long  a, b, c, maxV = 0;
            String input;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            grid = new int[n][m];
            for(int i = 0; i < n; i ++){
                input = br.readLine();
                for(int j = 0; j < m; j ++){
                    grid[i][j] = input.charAt(j) -'0';
                }
            }
            // case 1
            for(int i = 1; i <= m - 2; i++){
                   a = calcSum(0, 0, n - 1, i - 1);
                for(int j = i + 1; j <= m - 1; j++){
                    b = calcSum(0, i, n - 1, j - 1);
                    c = calcSum(0, j, n - 1, m - 1);
                    maxV = Math.max(maxV, a * b * c);
                }
            }

            // case 2
            for(int i = 1; i <= n - 2; i++){
                a = calcSum(0, 0, i - 1, m - 1);
                for(int j = i + 1; j <= n - 1; j++){
                    b = calcSum(i, 0, j - 1, m - 1);
                    c = calcSum(j, 0, n - 1, m - 1);
                    maxV = Math.max(maxV, a * b * c);
                }
            }

            // case 3
            for(int i = 0; i <= n - 2; i++){
                a = calcSum(i + 1, 0, n - 1, m - 1);
                for(int j = 1; j <= m - 1; j++){
                    b = calcSum(0, 0, i, j - 1);
                    c = calcSum(0, j, i, m - 1);
                    maxV = Math.max(maxV, a * b * c);
                }
            }

            // case 4
            for(int i = 0; i <= n - 2; i++){
                a = calcSum(0, 0, i, m - 1);
                for(int j = 1; j <= m - 1; j++){
                    b = calcSum(i + 1, 0, n - 1, j - 1);
                    c = calcSum(i + 1, j, n - 1, m - 1);
                    maxV = Math.max(maxV, a * b * c);
                }
            }

            // case 5
            for(int i = 1; i <= m - 1; i++){
                a = calcSum(0, 0, n - 1, i - 1);
                for(int j = 1; j <= n - 1; j++){
                    b = calcSum(0, i, j - 1, m - 1);
                    c = calcSum(j, i, n - 1, m - 1);
                    maxV = Math.max(maxV, a * b * c);
                }
            }

            // case 6
            for(int i = 1; i <= m - 1; i++){
                a = calcSum(0, i, n - 1, m - 1);
                for(int j = 1; j <= n - 1; j++){
                    b = calcSum(0, 0, j - 1, i - 1);
                    c = calcSum(j, 0, n - 1, i - 1);
                    maxV = Math.max(maxV, a * b * c);
                }
            }
            System.out.println(maxV);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1451
