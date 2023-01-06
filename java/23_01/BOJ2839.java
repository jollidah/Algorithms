import java.io.*;
import java.util.Arrays;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int target = Integer.parseInt(br.readLine());
        int[] dp = new int[target + 5];   # if 문을 활용한 예외처리 보단 리스트 길이를 늘려주는게 효율적
        final int MAX = Integer.MAX_VALUE;
        Arrays.fill(dp, MAX);
        dp[0] = 0;
        for (int i = 0; i < target; i++)
        {
            if (dp[i] != MAX)  
            {
                dp[i + 5] = Math.min(dp[i + 5], dp[i] + 1);
                dp[i + 3] = Math.min(dp[i + 3], dp[i] + 1);
            }
        }
        int res = (dp[target] == MAX) ? -1: dp[target];
        bw.write(String.valueOf(res));
        bw.close();
        br.close();
    }
}

# https://www.acmicpc.net/problem/2839
