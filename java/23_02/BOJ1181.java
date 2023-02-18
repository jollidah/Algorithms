// 단어 정렬

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        try {
            int n;
            String tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            PriorityQueue<String> pq = new PriorityQueue<>((s1, s2) -> {
                if (s1.length() != s2.length()) {
                    return s1.length() - s2.length();
                } else {
                    for (int i = 0; i < s1.length(); i++) {
                        if (s1.charAt(i) != s2.charAt(i)) {
                            return s1.charAt(i) - s2.charAt(i);
                        }
                    }
                    return 0;
                }
            });
            HashSet<String> hs = new HashSet<>();
            n = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++) {
                hs.add(br.readLine());
            }
            pq.addAll(hs);
            while (!pq.isEmpty()) {
                tmp = pq.poll();
                bw.write(String.format("%s\n", tmp));
            }
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1181
