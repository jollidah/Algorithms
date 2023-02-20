// 흙길 보수하기

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        try {
            long n, l, cnt = 0, end = 0;
            long []tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> (int)(a[0] - b[0]));
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Long.parseLong(st.nextToken());
            l = Long.parseLong(st.nextToken());
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                pq.add(new long[]{Long.parseLong(st.nextToken()), Long.parseLong(st.nextToken())});
            }
            while (!pq.isEmpty()) {
                tmp = pq.poll();
                end = Math.max(end, tmp[0]);
                while (end < tmp[1]) {
                    end += l;
                    cnt++;
                }
            }
            System.out.println(cnt);
        } catch (Exception e) {
        }
    }
}

// https://www.acmicpc.net/problem/1911
