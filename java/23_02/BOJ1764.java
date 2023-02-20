// 듣보잡

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        try {
            int n, m;
            ArrayList <String> dbList = new ArrayList<>();
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringBuilder sb = new StringBuilder();
            HashSet<String> hs = new HashSet<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            for (int i = 0; i < n; i++) {
                hs.add(br.readLine());
            }for (int i = 0; i < m; i++) {
                String tmp = br.readLine();
                if (hs.contains(tmp)) {
                    dbList.add(tmp);
                }
            }
            bw.write(String.valueOf(dbList.size()) + "\n");
            dbList.sort(Comparator.naturalOrder());
            for (String tmp : dbList) {
                bw.write(tmp);
                bw.write("\n");
            }
            bw.flush();
        } catch (Exception e) {
        }
    }
}

// https://www.acmicpc.net/problem/1764
