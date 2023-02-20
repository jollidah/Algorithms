// 나이순 정렬

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        try {
            int n;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st;
            ArrayList<String[]> al = new ArrayList<>();
            n = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                al.add(new String[]{st.nextToken(), st.nextToken()});
            }
            al.sort((a, b) -> Integer.parseInt(a[0]) - Integer.parseInt(b[0]));
            for (String[] tmp : al) {
                bw.write(String.format("%s %s\n", tmp[0], tmp[1]));
            }
            bw.flush();
        } catch (Exception e) {
        }
    }
}

// https://www.acmicpc.net/problem/10814
