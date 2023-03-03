// 퍼즐

import java.util.*;
import java.io.*;

public class BOJ1525.java {
    static StringBuilder sb;
    // 중복 방지할 HashMap
    static HashMap <String, Integer> hm = new HashMap<>();

    // 왼쪽으로 이동
    static String moveLeft(String s, int idx){
        char tc = s.charAt(idx);
        sb = new StringBuilder(s);
        sb.setCharAt(idx, s.charAt(idx - 1));
        sb.setCharAt(idx - 1, tc);
        return sb.toString();
    }

    // 오른쪽으로 이동
    static String moveRight(String s, int idx) {
        char tc = s.charAt(idx);
        sb = new StringBuilder(s);
        sb.setCharAt(idx, s.charAt(idx + 1));
        sb.setCharAt(idx + 1, tc);
        return sb.toString();
    }

    // 위로 이동
    static String moveUp(String s, int idx){
        char tc = s.charAt(idx);
        sb = new StringBuilder(s);
        sb.setCharAt(idx, s.charAt(idx - 3));
        sb.setCharAt(idx - 3, tc);
        return sb.toString();
    }

    // 아래로 이동
    static String moveDown(String s, int idx){
        char tc = s.charAt(idx);
        sb = new StringBuilder(s);
        sb.setCharAt(idx, s.charAt(idx + 3));
        sb.setCharAt(idx + 3, tc);
        return sb.toString();
    }

    static void bfs(String input){
        Queue <String> q = new LinkedList<>();
        String tmp, changed;
        int idx, cost;
        q.add(input);
        hm.put(input, 0);
        while(!q.isEmpty()){
            tmp = q.poll();
            if(tmp.equals("123456780")){
                if(hm.containsKey(tmp)){
                    System.out.println(hm.get(tmp));
                    System.exit(0);
                }
            } else{
                idx = tmp.indexOf("0");
                cost = hm.get(tmp);

                // 빈칸이 왼쪽으로
                if(idx % 3 != 0){
                    changed = moveLeft(tmp, idx);
                    if(!hm.containsKey(changed)){
                        hm.put(changed, cost + 1);
                        q.add(changed);
                    }
                }

                // 빈칸이 오른쪽으로
                if(idx % 3 != 2){
                    changed = moveRight(tmp, idx);
                    if(!hm.containsKey(changed)){
                        hm.put(changed, cost + 1);
                        q.add(changed);
                    }
                }

                // 빈칸이 위쪽으로
                if(idx / 3 != 0){
                    changed = moveUp(tmp, idx);
                    if(!hm.containsKey(changed)){
                        hm.put(changed, cost + 1);
                        q.add(changed);
                    }
                }

                // 빈칸이 아래쪽으로
                if(idx / 3 != 2){
                    changed = moveDown(tmp, idx);
                    if(!hm.containsKey(changed)){
                        hm.put(changed, cost + 1);
                        q.add(changed);
                    }
                }
            }
        }
        System.out.println(-1);
    }



    public static void main(String[] args) {
        try {
            int zy = 0, zx = 0;
            String tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st;
            sb= new StringBuilder();
            for(int i = 0; i < 3; i ++){
                st = new StringTokenizer(br.readLine());
                for(int j = 0; j < 3; j ++){
                    sb.append(Integer.parseInt(st.nextToken()));
                }
            }
            bfs(sb.toString());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1525