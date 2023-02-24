// 한수

import java.util.*;
import java.io.*;

public class Main {

    static boolean check(int n){
        String num = String.valueOf(n);
        if(num.length() >= 2){
            int d = num.charAt(1) - num.charAt(0);
            for(int i = 0; i < num.length() - 1;i++){
                if(num.charAt(i + 1) - num.charAt(i) != d){
                    return false;
                }
            }
            return true;
        } else{
            return true;
        }
    }

    public static void main(String[] args) {
        try {
            int n, cnt = 0;
            String input;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            n = Integer.parseInt(br.readLine());
            for (int i = 1; i <= n; i++) {
                if(check(i)){
                    cnt++;
                }
            }
            System.out.println(cnt);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1065
