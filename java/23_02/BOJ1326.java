// 폴짝폴짝

import java.util.*;
import java.io.*;

public class Main {

    static int [] dp;
    static int [] table;
    static int n;

    static void dfs(int pos, int cnt, int target) {
//        System.out.println(pos);
        if (pos == target) {
            dp[target] = Math.min(dp[target], cnt);
        } else {
            if(dp[pos] > cnt) {
                dp[pos] = cnt;
                int s = pos % table[pos] == 0 ? table[pos] :  pos % table[pos];
                for (; s <= n; s += table[pos]) {
                    dfs(s, cnt + 1, target);
                }
            }
        }
    }

    public static void main(String[] args) {

        try {
            int start = 0, target = 0;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            dp = new int[n + 1];
            table = new int[n + 1];
            Arrays.fill(dp, Integer.MAX_VALUE);
            for(int i = 1; i <= n; i++){
                table[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            start = Integer.parseInt(st.nextToken());
            target = Integer.parseInt(st.nextToken());

            dfs(start, 0, target);
            System.out.println(dp[target] == Integer.MAX_VALUE ? -1 : dp[target]);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1326
