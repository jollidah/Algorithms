// 카드 정렬하기

import java.util.*;
import java.io.*;

public class Main {
//
//    public static int dfs(ArrayList<Integer> gv, ArrayList<Integer> iv, int cnt) {
//        if (gv.isEmpty()) {
//            return cnt;
//        } else {
//            for(int )
//        }
//    }

    public static void main(String[] args) {
        try {
            int n;
            long tmp, a, b, sum, res = 0;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            n = Integer.parseInt(br.readLine());
            PriorityQueue<Long> pq = new PriorityQueue<>();
            for (int i = 0; i < n; i++) {
                tmp = Integer.parseInt(br.readLine());
                pq.add(tmp);
            }
            for (int i = 0; i < n - 1; i++) {
                a = pq.poll();
                b = pq.poll();
                sum = a + b;
                res += sum;
                pq.add(sum);
            }
            System.out.println(res);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1715
