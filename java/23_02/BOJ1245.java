// 농장관리

import java.util.*;
import java.io.*;

public class Main {
    static int n, m;

    static int[][] table;
    static int cnt = 0;
    static int []dx = new int[] {-1, -1, 0, 1, 1, 1, 0, -1};
    static int []dy = new int []{0, 1, 1, 1, 0, -1, -1, -1};

    static boolean [][] isVisit;

    static boolean dfs(int y, int x, boolean inf){
//            System.out.printf("%d %d\n", y, x);
            int height = table[y][x];
            isVisit[y][x] = true;
            boolean isTop = true;
            for(int i = 0; i < 8; i ++){
                int tmpY = y + dy[i];
                int tmpX = x + dx[i];
                if((n > tmpY && tmpY >= 0) && (m > tmpX && tmpX >= 0)){
                    if(table[tmpY][tmpX] > height){
                        isTop = false;
                    } else if(table[tmpY][tmpX] == height){
                        if(!isVisit[tmpY][tmpX]){
                            isTop = dfs(tmpY, tmpX, isTop & inf);
                        }
                    }
                }
            }
            return isTop & inf;
        }

    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            table = new int[n][m];
            isVisit = new boolean [n][m];
            for(int i = 0; i < n; i ++){
                Arrays.fill(isVisit[i], false);
            }
            for(int i = 0; i < n; i ++){
                st = new StringTokenizer(br.readLine());
                for(int j = 0; j < m; j ++){
                    table[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            for(int i = 0; i < n; i ++){
                for(int j = 0; j < m; j ++){
                    if(!isVisit[i][j] && dfs(i, j, true)){
//                        System.out.printf("%d %d\n", i, j);
                        cnt++;
                    }
                }
            }
            System.out.println(cnt);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1245
