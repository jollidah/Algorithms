// N과 M(1)

import java.io.*;
import java.util.*;

public class Main {

    public static void DPS(String s1, String s2, int m){
        if (s1.length() == 2 * m){
            System.out.println(s1);
        }
        else{
            for(int i = 0; i < s2.length() - 1; i++){
                DPS(s1 + s2.charAt(i) + " ", s2.substring(0, i) + s2.substring(i + 1), m);
            }
            DPS(s1 + s2.charAt(s2.length() - 1) + " ", s2.substring(0, s2.length() - 1), m);
        }
    }

    public static void main(String[] args) {
        int n, m;
        String s2 = "";
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            for(int i = 1; i <= n; i++){
                s2 += String.valueOf(i);
            }
            DPS("", s2, m);
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/15649
