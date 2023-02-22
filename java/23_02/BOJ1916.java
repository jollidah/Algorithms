// 최소 비용 구하기

import java.util.*;
import java.io.*;

public class Main {

    static ArrayList<Edge>[] table;
    static int [] dp;

    static class Edge {
        int e, c;

        Edge(int e, int c) {
            this.e = e;
            this.c = c;
        }
    }

    static int n;
    public static void main(String[] args) {
        try {
            int m, tmpX, tmpY, tmpCost;
            int [] tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st;
            n = Integer.parseInt(br.readLine());
            m = Integer.parseInt(br.readLine());
            PriorityQueue<Edge> pq = new PriorityQueue<>((a, b) -> a.c - b.c);
            table = new ArrayList [n + 1];
            dp = new int [n + 1];
            Arrays.fill(dp, Integer.MAX_VALUE);
            for(int i = 1; i <= n; i ++){
                table[i] = new ArrayList<Edge>();
            }
            while(m-- > 0) {
                st = new StringTokenizer(br.readLine());
                tmpX = Integer.parseInt(st.nextToken());
                tmpY = Integer.parseInt(st.nextToken());
                tmpCost = Integer.parseInt(st.nextToken());
                table[tmpX].add(new Edge(tmpY, tmpCost));
            }
            st = new StringTokenizer(br.readLine());
            tmpX = Integer.parseInt(st.nextToken());
            tmpY = Integer.parseInt(st.nextToken());
            pq.add(new Edge(tmpX, 0));
            while (!pq.isEmpty()) {
                Edge e = pq.poll();
                if (e.e == tmpY) {
                    System.out.println(e.c);
                    break;
                }
                if(dp[e.e] > e.c){
                    dp[e.e] = e.c;
                    for (Edge tmpE : table[e.e]) {
                        pq.add(new Edge(tmpE.e, tmpE.c + e.c));
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1916
