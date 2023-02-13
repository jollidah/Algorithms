import java.io.*;

public class n01720 {

	static int N;
	static int[] dp = new int[31];
	static int[][] dp2 = new int[31][31];

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		N = Integer.parseInt(br.readLine());

		dp[1] = 1;
		dp[2] = 3;
		for (int i = 3; i <= N; i++) {
			dp[i] = dp[i - 1] + dp[i - 2] * 2;
		}

		if (N % 2 == 0) {  // N이 짝수일 때
			dp2[N / 2][N / 2 + 1] = 3;
			dp2[N / 2 - 1][N / 2 + 2] = 5;
			
			int i = N / 2 - 2;
			int j = N / 2 + 3;
			while (i >= 1 && j <= N) {
				dp2[i][j] = dp2[i + 1][j - 1] + dp2[i + 2][j - 2] * 2;
				i--;
				j++;
			}
		}

		else {  // N이 홀수일 때
			dp2[N / 2 + 1][N / 2 + 1] = 1;
			dp2[N / 2][N / 2 + 2] = 1;
			
			int i = N / 2 - 1;
			int j = N / 2 + 3;
			while (i >= 1 && j <= N) {
				dp2[i][j] = dp2[i + 1][j - 1] + dp2[i + 2][j - 2] * 2;
				i--;
				j++;
			}
		}

		int res = (dp[N] - dp2[1][N]) / 2 + dp2[1][N]; // 최종 결과

		bw.write(res + "\n");
		bw.flush();

	}

}
