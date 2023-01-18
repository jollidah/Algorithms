import java.io.*;
import java.util.*;

// 다각형의 면적

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        float[] x = new float[n + 1];
        float[] y = new float[n + 1];
        float sum_a = 0, sum_b = 0;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            x[i] = Integer.parseInt(st.nextToken());
            y[i] = Integer.parseInt(st.nextToken());
        }

        x[n] = x[0];
        y[n] = y[0];

        for (int i = 0; i < n; i++) {
            sum_a += x[i] * y[i + 1];
            sum_b += x[i + 1] * y[i];
        }
        // 0.1f 는 소수 첫째 자리까지 표현 즉, 두번째 자리에서 반올림
        String area = String.format("%.1f", (Math.abs(sum_a - sum_b) / 2.0));
        bw.write(area);

        br.close();
        bw.flush();
        bw.close();
    }
}

# https://www.acmicpc.net/problem/2166
