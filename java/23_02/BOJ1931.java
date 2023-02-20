// 회의실 배정

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        try {
            int n, cnt = 0, pos;
            int []tmp;
            PriorityQueue <int[]> pq = new PriorityQueue<>((a, b) -> a[1] == b[1] ? a[0] - b[0] : a[1] - b[1]);
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            n = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                pq.add(new int[]{Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())});
            }
            pos = 0;
            while (!pq.isEmpty()) {
                tmp = pq.poll();
                if (pos <= tmp[0]) {
                    cnt++;
                    pos = tmp[1];
                }
            }
            System.out.println(cnt);
        } catch (Exception e) {
        }
    }
}

// https://www.acmicpc.net/problem/1931
