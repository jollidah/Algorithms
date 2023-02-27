// 타일 코드

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        try {
            int n, res = 0;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            n = Integer.parseInt(br.readLine());
            int [] dp = new int [n + 1];
            dp[0] = 1;
            dp[1] = 1;
            if(n < 2){
                System.out.println(dp[n]);
                System.exit(0);
            }
            for(int i = 2; i <= n; i++){
                dp[i] = dp[i - 1] + dp[i - 2] * 2;
            }
            if(n % 2 == 1){
                res = (dp[n] + dp[n / 2]) / 2;
            } else {
                res = (dp[n / 2 - 1] * 2 + dp[n / 2] + dp[n]) / 2;
            }
            System.out.println(res);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1720
