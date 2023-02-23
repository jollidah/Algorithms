// 줄어드는 수

import java.io.*;
import java.util.*;

class Main{

    static int n;
    static long res = -1;
    static boolean found = false;
    static void dfs(int lim, int depth) {
        for(int i = depth; i < lim; i ++){
            if(depth == 0){
                n--;
                if(n == 0){
                    found = true;
                    res = i;
                    break;
                }
            } else{
                dfs(i, depth - 1);
                if (found) {
                    res += i * (long)Math.pow(10, depth);
                    break;
                }
            }
        }
    }

    public static void main(String[] args) {
        try {
            StringBuilder sb = new StringBuilder();
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            n = Integer.parseInt(br.readLine());
            for (int i = 0; i < 10 && !found; i++) {
                dfs(10, i);
            }
            System.out.println(res);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

// https://www.acmicpc.net/problem/1174
