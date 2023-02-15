// 수강신청

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        try {
            int capacity, n;
            String tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st = new StringTokenizer(br.readLine());
            capacity = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
            LinkedHashSet<String> lhs = new LinkedHashSet<>();  
            for (int j = 0; j < n; j++) {
                tmp = br.readLine();
                lhs.remove(tmp);    // 포함되어 있지 않더라도 에러를 내지 않는다
                lhs.add(tmp);
            }
            Iterator<String> iter = lhs.iterator(); // LinkedHashSet은 인덱스 하나하나 꺼내볼 수 없다.
            for (int j = 0; iter.hasNext() && j < capacity ; j++) {
                bw.write(iter.next());
                bw.write("\n");
            }
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/13414
