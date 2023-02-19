// 부분순열의 합

import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int [] arr;
    static int n, s, cnt = 0;
    public static void dfs(int pos, int k) {
        if (pos == n) {
            if (k == s) {
                cnt++;
                return;
            }
        } else {
            dfs(pos + 1, k + arr[pos]);
            dfs(pos + 1, k);
        }
    }

    public static void main(String[] args){
        try {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            s = Integer.parseInt(st.nextToken());
            arr = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                int tmp = Integer.parseInt(st.nextToken());
                arr[i] = tmp;
            }
            if (s == 0) {
                cnt = -1;
            }
            dfs(0, 0);
            System.out.println(cnt);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1182
