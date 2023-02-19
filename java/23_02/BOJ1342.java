// 행운의 문자열

import java.io.*;
import java.util.*;


public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int cnt = 0;

    static void dfs(char ex, HashMap<Character, Integer> hm, int exitNum) {
        if (exitNum == 0) {
            cnt++;
        } else {
            for (char tmp : hm.keySet()){
                if (tmp != ex) {
                    int wNum = hm.get(tmp);
                    if (wNum != 0) {
                        hm.replace(tmp, wNum - 1);
                        dfs(tmp, hm, exitNum - 1);
                        hm.replace(tmp, wNum);
                    }
                }
            }
        }
    }

    public static void main(String[] args){
        try {
            String s = br.readLine();
            HashMap<Character, Integer> hm = new HashMap<>();
            for (int i = 0; i < s.length(); i++) {
                char tmp = s.charAt(i);
                if (hm.containsKey(tmp)) {
                    hm.put(tmp, hm.get(tmp) + 1);
                } else {
                    hm.put(tmp, 1);
                }
            }
            dfs('.', hm, s.length());
            System.out.println(cnt);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1342
