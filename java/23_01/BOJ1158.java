// 요세푸스 문제

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        LinkedList<Integer> table = new LinkedList<>();
        int n, k, idx;
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());
            br.close();
            bw.write("<");
            for (int i = 1; i <= n; i++){
                table.add(i);
            }
            idx = -1;
            while((n = table.size()) > 1){
                idx += k;
                idx = idx >= n? idx % n: idx;
                bw.write(String.valueOf(table.get(idx)) + ", ");
                table.remove(idx--);    // 뺀 만큼 인덱스도 줄어야 함
            }
            bw.write(String.valueOf(table.getFirst()) + ">");
            bw.flush();
            bw.close();
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1158
