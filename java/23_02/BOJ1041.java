// 주사위

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        try {
            int n;
            long oneMin, twoMin, threeMin, res = 0;
            int [] table = new int[6];
            int [] pair = new int [] {5, 4, 3, 2, 1, 0};
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 6; i++) {
                table[i] = Integer.parseInt(st.nextToken());
            }
            twoMin = Integer.MAX_VALUE;
            threeMin = Integer.MAX_VALUE;
            for (int i = 0; i < 4; i++) {
                for (int j = i + 1; j < 5; j++) {
                    if (j != pair[i]) {
                        for (int k = j + 1; k < 6; k++) {
                            if (k != pair[i] && k != pair[j]) {
                                threeMin = Math.min(threeMin, table[i] + table[j] + table[k]);
                            }
                        }
                    }
                }
            }
            for (int i = 0; i < 5; i++) {
                for (int j = i + 1; j < 6; j++) {
                    if (j != pair[i]) {
                        twoMin = Math.min(twoMin, table[i] + table[j]);
                    }
                }
            }
            Arrays.sort(table);
            oneMin = table[0];

            if (n > 2) {
                res += oneMin * (n - 2) * (n - 2) * 5;
                res += twoMin * (n - 2) * 8;
                res += oneMin * (n - 2) * 4;
            }
            res += threeMin * 4 + twoMin * 4;
            if (n == 1) {
                res = table[0] + table[1] +table[2] +table[3] +table[4];
            }
            System.out.println(res);
        } catch (Exception e) {
        }
    }
}

// https://www.acmicpc.net/problem/1041
