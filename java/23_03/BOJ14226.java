// 이모티콘

//import java.util.*;
//import java.io.*;
//
//public class Main {
//    public static void main(String[] args) {
//        try {
//            int n, minV = 1000;
//            int [] tmp;
//            HashMap<Integer, Integer> hm = new HashMap<>();
//            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//            StringTokenizer st = new StringTokenizer(br.readLine());
//            PriorityQueue <int[]> pq = new PriorityQueue<>((a, b) -> b[0] - a[0]);
//            n = Integer.parseInt(st.nextToken());
//            pq.add(new int[] {1, 0, 0});
//            while(!pq.isEmpty()){
//                tmp = pq.poll();
//                System.out.println(tmp[0]);
//                if(tmp[0] == n){
//                    minV = Math.min(minV, tmp[2]);
//                }else {
//                    if (hm.containsKey(tmp[0])){
//                        if(hm.get(tmp[0]) <= tmp[2]){
//                            continue;
//                        }
//                    } else{
//                        hm.put(tmp[0], tmp[2]);
//                    }
//                    if (tmp[0] < n) {
//                        pq.add(new int[]{tmp[0] + tmp[1], tmp[1], tmp[2] + 1});
//                        pq.add(new int[]{tmp[0], tmp[0], tmp[2] + 1});
//                    }
//                    pq.add(new int[]{tmp[0] - 1, tmp[1], tmp[2] + 1});
//                }
//            }
//            System.out.println(minV);
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
//    }
//}

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        try {
            int n;
            int [] tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            Queue <int[]> q = new LinkedList<>();
            n = Integer.parseInt(st.nextToken());
            boolean [][]isVisit = new boolean [1025][1025];
            isVisit[1][0] = true;
            isVisit[0][0] = true;
            q.add(new int[] {1, 0, 0});
            while(!q.isEmpty()){
                tmp = q.poll();
                if(tmp[0] == n){
                    System.out.println(tmp[2]);
                    System.exit(0);
                } else {
                    if(tmp[0] < n){
                        if (tmp[1] != tmp[0] && !isVisit[tmp[0]][tmp[0]]){
                            q.add(new int [] {tmp[0], tmp[0], tmp[2] + 1});
                            isVisit[tmp[0]][tmp[0]] = true;
                        }
                        if(tmp[0] + tmp[1] <= 1024 && tmp[1] != 0 && !isVisit[tmp[0] + tmp[1]][tmp[1]]){
                            q.add(new int [] {tmp[0] + tmp[1], tmp[1], tmp[2] + 1});
                        }
                    }
                    if (tmp[0] - 1 > 2 && !isVisit[tmp[0] - 1][tmp[1]]){
                        q.add(new int [] {tmp[0] - 1, tmp[1], tmp[2] + 1});
                        isVisit[tmp[0] - 1][tmp[1]] = true;
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}



// https://www.acmicpc.net/problem/14226
