// 암호 만들기

import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static HashSet <String> hs  = new HashSet<String>(Arrays.asList("a", "e","i", "o", "u"));
    static String [] al;
    static String [] arr;
    static StringBuilder sb = new StringBuilder();
    static void dfs(int resCon, int resVow, int ptr, int cnt){
        if(ptr == m){
            if(cnt == n && resCon <= 0 && resVow <= 0){
                for(int i = 0; i < n; i ++){
                    sb.append(arr[i]);
                }
                sb.append("\n");
            }
        } else {
            if (cnt < n){
                arr[cnt] = al[ptr];
                if(hs.contains(al[ptr])){
                    dfs(resCon, resVow - 1, ptr + 1, cnt + 1);
                } else{
                    dfs(resCon - 1, resVow, ptr + 1, cnt + 1);
                }
            }
            dfs(resCon, resVow, ptr + 1, cnt);
        }

    }

    public static void main(String[] args) {
        try {
            String tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            arr = new String [n];
            al = new String [m];
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < m; i ++){
                al[i] = st.nextToken();
            }
            Arrays.sort(al);
            dfs(2, 1, 0, 0);
            bw.write(sb.toString());
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1759
