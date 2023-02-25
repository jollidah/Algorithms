// N과 M(3)

import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[] arr;
    static StringBuilder sb = new StringBuilder();

    static void dfs(int cnt){
        if(cnt == m){
            for(int i = 0; i < m; i++){
                sb.append(arr[i] + " ");
            }
            sb.append("\n");
        } else {
            for(int i = 1; i <= n; i++){
                arr[cnt] = i;
                dfs(cnt + 1);
            }
        }
    }

    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            arr = new int[m];
            dfs(0);
            System.out.println(sb);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/15651
