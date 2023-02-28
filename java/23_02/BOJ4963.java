// 섬의 개수

import java.util.*;
import java.io.*;

public class Main {
    static boolean [][] toVisit;
    static int n, m;

    static int [] dx = new int[] {0, 1, 1, 1, 0, -1, -1, -1};
    static int [] dy = new int [] {1, 1, 0, -1, -1, -1, 0, 1};
    static void dfs(int y, int x){
        toVisit[y][x] = false;
        for(int i = 0; i < 8; i ++){
            int tmpY = y + dy[i];
            int tmpX = x + dx[i];
            if(tmpY >= 0 && tmpY < n && tmpX >= 0 && tmpX < m){
                if(toVisit[tmpY][tmpX]){
                    dfs(tmpY, tmpX);
                }
            }
        }
    }

    public static void main(String[] args) {
        try {
            int cnt;
            int [] tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st;

            while(true){
                st = new StringTokenizer(br.readLine());
                m = Integer.parseInt(st.nextToken());
                n = Integer.parseInt(st.nextToken());
                if(n == 0 && m == 0){break;}

                cnt = 0;
                toVisit = new boolean [n][m];
                Queue <int []> q = new LinkedList<>();
                for(int i = 0; i < n; i++){
                    st = new StringTokenizer(br.readLine());
                    for(int j = 0; j < m; j++){
                        if (st.nextToken().equals("1")){
                            toVisit[i][j] = true;
                            q.add(new int[] {i, j});
                        }
                    }
                }
                while(!q.isEmpty()){
                    tmp = q.poll();
                    if(toVisit[tmp[0]][tmp[1]]){
                        dfs(tmp[0], tmp[1]);
                        cnt++;
                    }
                }
                bw.write(String.valueOf(cnt));
                bw.write("\n");
            }
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/4963
