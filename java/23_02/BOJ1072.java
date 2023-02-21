// 게임 3

import java.util.*;
import java.io.*;

public class Main {

    static long calc(long y, long x, long alpha) {
        return 100 * (y + alpha) / (x + alpha);
    }

    public static void main(String[] args) {

        try {
            long x, y, mid, lp, rp, res;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            x = Long.parseLong(st.nextToken());
            y = Long.parseLong(st.nextToken());
            res = - 1;
            lp = 0;
            rp = (long) 2e9;
            long standard = 100 * y / x;
            while (lp < rp) {
                mid = (lp + rp) / 2;
                if (calc(y, x, mid) > standard) {
                    rp = mid;
                    res = mid;
                } else {
                    lp = mid + 1;
                }
            }
            System.out.println(res);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1072
