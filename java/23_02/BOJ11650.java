// 좌표 정렬하기

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        try {
            int n, x, y;
            int[] tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
            n = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                x = Integer.parseInt(st.nextToken());
                y = Integer.parseInt(st.nextToken());
                pq.add(new int [] {x, y});
            }
            while (!pq.isEmpty()) {
                tmp = pq.poll();
                bw.write(String.format("%d %d\n", tmp[0], tmp[1]));
            }
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/11650
