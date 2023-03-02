// 연결 요소의 개수

import java.util.*;
import java.io.*;

public class Main {
    static int []p;
    static HashSet <Integer> hs = new HashSet<>();
    static int parent(int a){
        while(p[a] != a){
            a = p[a];
        }
        return p[a];
    }

    static void union(int a, int b){
        int ap = parent(a);
        int bp = parent(b);
        if(ap != bp){
            if(ap > bp){
                p[ap] = bp;
                hs.remove(ap);
            } else{
                p[bp] = ap;
                hs.remove(bp);
            }
        }
    }

    public static void main(String[] args) {
        try {
            int n, m;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st= new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            p = new int [n + 1];
            for(int i = 1; i <= n; i ++){
                hs.add(i);
                p[i] = i;
            }
            while(m-- > 0){
                st= new StringTokenizer(br.readLine());
                union(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            }
            System.out.println(hs.size());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/11724
