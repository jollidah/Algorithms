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
            // 예외 처리
            if(n < 2){
                System.out.println(dp[n]);
                System.exit(0);
            }
            for(int i = 2; i <= n; i++){
                dp[i] = dp[i - 1] + dp[i - 2] * 2;
            }
            if(n % 2 == 1){
                // 홀수는 가운데가 1짜리 블록 고정하기 때문에 2로 나누기만 하면 된다.
                res = (dp[n] + dp[n / 2]) / 2;
            } else {
                // 짝수는 두가지 경우로 나눠야 한다 가운데가 세로로된 블록과 그 외의 블록
                res = (dp[n / 2 - 1] * 2 + dp[n / 2] + dp[n]) / 2;
            }
            System.out.println(res);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1720
