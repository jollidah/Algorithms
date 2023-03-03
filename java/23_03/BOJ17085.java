// 십자가 2개 

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


public class Main {


    static int [] dx = new int[] {0, 1, 0, -1};
    static int [] dy = new int[] {1, 0, -1, 0};
    static int n, m, maxV = 0;
    static boolean[][] toVisit;
    static int[][] comb = new int[2][2];

    // 좌표와 십자가 크기를 바탕으로 가능한지 확인
    public static boolean check(int l1, int l2){
        int tmpY, tmpX;
        int y1 = comb[0][0];
        int x1 = comb[0][1];
        int y2 = comb[1][0];
        int x2 = comb[1][1];
        boolean res = true;
        boolean [][] tmpVisit = new boolean[n][m];

        // 배열 깊은 복사 (2차원 배열)
        for(int i = 0; i < n; i ++){
            tmpVisit[i] = toVisit[i].clone();
        }
        tmpVisit[y1][x1] = false;
        tmpVisit[y2][x2] = false;
        for (int i = 0; res && i < 4; i ++){
            for(int j = 1; res && j <= l1; j++){
                tmpY = y1 + j * dy[i];
                tmpX = x1 + j * dx[i];
                if(tmpY >= 0 && tmpY < n && tmpX >=0 && tmpX < m){
                    res &= tmpVisit[tmpY][tmpX];
                    tmpVisit[tmpY][tmpX] = false;
                } else{
                    res = false;
                }
            }
        }

        for (int i = 0; res && i < 4; i ++){
            for(int j = 1; res && j <= l2; j++){
                tmpY = y2 + j * dy[i];
                tmpX = x2 + j * dx[i];
                if(tmpY >= 0 && tmpY < n && tmpX >=0 && tmpX < m){
                    res &= tmpVisit[tmpY][tmpX];
                    tmpVisit[tmpY][tmpX] = false;
                } else{
                    res = false;
                }
            }
        }
        return res;
    }

    // 십자가 크기 중복 조합
    public static void simulate(){
        int l1, l2;
        for(int i = 0; i < 8; i ++){
            for(int j = 0; j < 8; j ++){
                l1 = i;
                l2 = j;
                // 가능하다면 최댓값 업데이트
                if(check(l1, l2)){
                    maxV = Math.max(maxV, (1 + 4 * l1) * (1 + 4 * l2));
                }
            }
        }
    }

    // 좌표 조합
    public static void dfs(int y, int x, int cnt){
        if(cnt == 2){
            simulate();
        } else if(y < n) {
            dfs(y + (x + 1) / m, (x + 1) % m, cnt);
            if (toVisit[y][x]){
                comb[cnt] = new int [] {y, x};
                dfs(y + (x + 1) / m, (x + 1) % m, cnt + 1);
            }
        }
    }


    public static void main(String[] args) {
        try {
            String tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            toVisit = new boolean[n][m];
            for(int i = 0; i < n; i ++){
                tmp = br.readLine();
                for(int j = 0; j < m; j ++){
                    if(tmp.charAt(j) == '#'){
                        toVisit[i][j] = true;
                    }
                }
            }
            dfs(0, 0, 0);
            System.out.println(maxV);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/17085
