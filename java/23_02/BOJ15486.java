// 퇴사2

import java.util.*;
import java.io.*;

public class Main {
     public static class Pair{
         int t, p;
        public Pair(int a, int b){
             this.t = a;
             this.p = b;
        }
    }

    public static void main(String[] args) {
        try {
            int n, a, b, tmpDate, maxV = 0;
            int [] dp;
            Pair [] table;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st;
            n = Integer.parseInt(br.readLine());
            dp = new int[n + 1];
            table = new Pair[n + 1];
            for(int i = 1; i <= n; i ++){
                st = new StringTokenizer(br.readLine());
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());
                Pair p = new Pair(a - 1, b);
                table[i] = p;
            }
            for(int i = 1; i <= n; i ++){
                tmpDate = i + table[i].t;
                if(tmpDate <= n){
                    dp[tmpDate] = Math.max(dp[tmpDate], maxV + table[i].p);
                }
                maxV = Math.max(maxV, dp[i]);
            }
            System.out.println(maxV);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/15486
