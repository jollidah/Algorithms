// 강의실

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        try {
            int n, e, t, s;
            int [] tmp;
            PriorityQueue <int[]> pq1 = new PriorityQueue<>((a, b) -> a[1] - b[1]);
            PriorityQueue <Integer> pq2 = new PriorityQueue<>();
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            n = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                t = Integer.parseInt(st.nextToken());
                s = Integer.parseInt(st.nextToken());
                e = Integer.parseInt(st.nextToken());
                pq1.add(new int[] {t, s, e});
            }
            pq2.add(0);
            while (!pq1.isEmpty()) {
                tmp = pq1.poll();
                e = pq2.poll();
                if (e <= tmp[1]) {
                    pq2.add(tmp[2]);
                } else {
                    pq2.add(e);
                    pq2.add(tmp[2]);
                }
            }
            System.out.println(pq2.size());
        } catch (Exception e) {
        }
    }
}

// https://www.acmicpc.net/problem/1374
