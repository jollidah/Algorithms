// 동전 1

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        try {
            int n, k, tmp, res;
            int []c;
            int [][] dp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());
            c = new int[n];
            dp = new int [n][k + 1];
            for(int j = 0; j < n; j ++){
                c[j] = -Integer.parseInt(br.readLine());
            }
            Arrays.sort(c);
            for(int j = 0; j < n; j ++){
                c[j] *= -1;
                if (c[j] <= k){
                    dp[j][c[j]] = 1;
                }
            }
            res = 0;
            for(int i = 1; i < k + 1; i ++){
                for(int j = 0; j < n; j ++){
                    if (dp[j][i] != 0){
                        for(int t = j ; t < n; t++){
                            tmp = i + c[t];
                            if(tmp <= k){
                                dp[t][tmp] += dp[j][i];
                            }
                        }
                    }
                }
            }
            for(int j = 0; j < n; j ++){
                res += dp[j][k];
            }
            System.out.println(res);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/2293
