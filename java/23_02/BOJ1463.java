// 1로 만들기

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int n = Integer.parseInt(br.readLine());
            int[] tmp = new int [] {n , 0};
            PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
            pq.add(tmp);
            while (!pq.isEmpty() && ((tmp = pq.poll())[0] != 1)) {
                if(tmp[0] % 3 == 0){pq.add(new int[] {tmp[0] / 3, tmp[1] + 1});}
                if(tmp[0] % 2 == 0){pq.add(new int[] {tmp[0] / 2, tmp[1] + 1});}
                pq.add(new int[] {tmp[0] - 1, tmp[1] + 1});
            }
            System.out.println(tmp[1]);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1463
