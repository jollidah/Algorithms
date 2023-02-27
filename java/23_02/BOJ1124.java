// 언더프라임

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        try {
            int n,m,cnt = 0;
            HashSet <Integer> hs = new HashSet<>();
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            int [] dp = new int[m + 1];
            boolean [] oTable = new boolean[m + 1];
            Arrays.fill(oTable, true);
            for(int i = 2; i <= m; i ++){
                if(oTable[i] == true){
                    hs.add(i);
                    int cur = i * 2;
                    while(cur <= m){
                        oTable[cur] = false;
                        cur += i;
                    }
                }
            }
            for(int i = 2; i <= m; i ++) {
                for (Integer j : hs) {
                    if(i % j == 0){
                        dp[i] = dp[i / j] + 1;
                        break;
                    }
                }
            }
            for (int i = n; i <= m; i++) {
                if(hs.contains(dp[i])){
                    cnt++;
                }
            }
            System.out.println(cnt);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1124
