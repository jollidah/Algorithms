// 유기농 배추

import java.io.*;
import java.util.*;

public class Main {
    public static int [][] table;
    public static int [][] cabbageList; // y, x 좌표
    public static int[] dx = {0, 1, 0, -1};
    public static int[] dy = {1, 0, -1, 0};
    public static int m, n;


    public static boolean needWorm(int y, int x) {
        if (table[y][x] == 0) {
            return false;
        } else {
            table[y][x] = 0;
            for (int i = 0; i < 4; i++) {
                int tmpY = y + dy[i];
                int tmpX = x + dx[i];
                if ((n > tmpY && tmpY >= 0) && (m > tmpX && tmpX >= 0)) {
                    needWorm(tmpY, tmpX);
                }
            }
            return true;
        }
    }

    public static void main(String[] args) {
        try {
            int t, k, x, y, cnt;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            t = Integer.parseInt(br.readLine());
            for (int q = 0; q < t; q++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                m = Integer.parseInt(st.nextToken());   // 가로
                n = Integer.parseInt(st.nextToken());   // 세로
                k = Integer.parseInt(st.nextToken());
                table = new int[n][m];
                cabbageList = new int[k][2];
                cnt = 0;
                for (int r = 0; r < k; r++) {
                    st = new StringTokenizer(br.readLine());
                    x = Integer.parseInt(st.nextToken());   // 가로
                    y = Integer.parseInt(st.nextToken());
                    table[y][x] = 1;
                    cabbageList[r][0] = y;
                    cabbageList[r][1] = x;
                }
                for (int[] tmp : cabbageList) {
                    if (needWorm(tmp[0], tmp[1])) {
                        cnt++;
                    }
                }
                bw.write(String.valueOf(cnt) + "\n");
            }
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1012
