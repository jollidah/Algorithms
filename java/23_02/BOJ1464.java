// 뒤집기 3

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        try {
            char head, tail;
            PriorityQueue <int[]> pq1 = new PriorityQueue<>((a, b) -> a[1] - b[1]);
            PriorityQueue <Integer> pq2 = new PriorityQueue<>();
            StringBuilder sb = new StringBuilder();
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String s = br.readLine();
            head = s.charAt(0);
            sb.append(head);
            for (int i = 1; i < s.length(); i++) {
                if (s.charAt(i) <= head) {
                    sb.insert(0, s.charAt(i));
                    head = s.charAt(i);
                } else {
                    sb.append(s.charAt(i));
                }
            }
            System.out.println(sb.toString());
        } catch (Exception e) {
        }
    }
}

// https://www.acmicpc.net/problem/1464
