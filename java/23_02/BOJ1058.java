// 친구

import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    public static void main(String[] args) throws NumberFormatException, IOException {
        int N = Integer.parseInt(br.readLine());
        int[][] table = new int[N][N];
        boolean[][] isFriend = new boolean[N][N];
        for(int i = 0; i < N; i++) {
            String tmp = br.readLine();
            for(int j = 0; j < N; j++) {
                char ch = tmp.charAt(j);
                if(ch == 'Y') {
                    table[i][j] = 1;
                    isFriend[i][j] = true;
                }
            }
        }

        for(int k = 0; k < N; k++) {
            for(int i = 0; i < N; i++) {
                if(i == k) continue;
                for(int j = 0; j < N; j++) {
                    if(j == k || j == i) continue;
                    if(table[i][k] == 1 && table[k][j] == 1) isFriend[i][j] = true;
                }
            }
        }
        int max = 0;
        for(int i = 0; i < N; i++) {
            int cnt = 0;
            for(int j = 0; j < N; j++) {
                if(isFriend[i][j]) cnt++;
            }
            max = cnt > max ? cnt :max;
        }
        System.out.println(max);
    }
}

//  https://www.acmicpc.net/problem/1058
