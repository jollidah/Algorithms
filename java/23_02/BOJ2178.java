// 미로 탐색

import java.util.*;
import java.io.*;

public class Main {


    public static void main(String[] args) {
        try {
            int [] dx = new int[] {0, 1, 0, -1};
            int [] dy = new int [] {1, 0, -1, 0};
            int n, m;
            int [] tmp;
            boolean [][] grid;
            boolean [][] isVisit;
            String input;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st = new StringTokenizer(br.readLine());
            PriorityQueue <int []> pq = new PriorityQueue<>((a, b) -> a[2] - b[2]);
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            grid = new boolean [n][m];
            isVisit = new boolean [n][m];
            for(int i = 0; i < n; i ++){
                input = br.readLine();
                for(int j = 0; j < m; j ++){
                    if(input.charAt(j) == '1'){
                        grid[i][j] = true;
                    }
                }
            }
            pq.add(new int [] {0, 0, 1});
            while(!pq.isEmpty()){
                tmp = pq.poll();
                if(tmp[0] == n -1 && tmp[1] == m - 1){
                    System.out.println(tmp[2]);
                    System.exit(0);
                }
                for(int i = 0; i < 4; i ++){
                    int tmpY = tmp[0] + dy[i];
                    int tmpX = tmp[1] + dx[i];
                    if(tmpY >= 0 && tmpY < n && tmpX >= 0 && tmpX < m){
                        if(grid[tmpY][tmpX] && !isVisit[tmpY][tmpX]){
                            isVisit[tmpY][tmpX] = true;
                            pq.add(new int [] {tmpY, tmpX, tmp[2] + 1});
                        }
                    }
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/2178
