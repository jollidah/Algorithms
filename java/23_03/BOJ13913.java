 // 숨바꼭질4
 
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
            int n, m, tmp;
            int [] [] dp = new int[2][200000];
            boolean [] isVisit = new boolean [200000];
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            Queue <Integer> q = new LinkedList<>();
            ArrayList <Integer> al = new ArrayList<>();
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            Arrays.fill(dp[0],Integer.MAX_VALUE);
            q.add(n);
            dp[0][n] = 0;
            isVisit[0] = true;
            isVisit[n] = true;

            // m이 n보다 작은 경우
            if (m < n){
                System.out.println(n - m);
                while(n >= m){
                    System.out.printf("%d ", n--);
                }
            } else{
                while(!q.isEmpty()){
                    tmp = q.poll();
                    if(tmp == m){
                        System.out.println(dp[0][tmp]);
                        break;
                    } else{
                        if(tmp < m && !isVisit[tmp * 2]){
                            isVisit[tmp * 2] = true;
                            dp[0][tmp * 2] = dp[0][tmp] + 1;
                            dp[1][tmp * 2] = tmp;
                            q.add(tmp * 2);
                        }
                        if(tmp < m && tmp + 1 < 100000 && !isVisit[tmp + 1]){
                            isVisit[tmp + 1] = true;
                            dp[0][tmp + 1] = dp[0][tmp] + 1;
                            dp[1][tmp + 1] = tmp;
                            q.add(tmp + 1);
                        }
                        if(tmp - 1 >= 0 && !isVisit[tmp - 1]){
                            isVisit[tmp - 1] = true;
                            dp[0][tmp - 1] = dp[0][tmp] + 1;
                            dp[1][tmp - 1] = tmp;
                            q.add(tmp - 1);
                        }
                    }
                }
                
                // 출처룰 추적
                tmp = m;
                while(tmp != n){
                    al.add(tmp);
                    tmp = dp[1][tmp];
                }
                System.out.printf("%d ", n);
                for(int i = al.size() - 1; i >= 0; i --){
                    System.out.printf("%d ", al.get(i));
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}


 
 // https://www.acmicpc.net/problem/13913
