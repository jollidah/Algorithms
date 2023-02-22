//DFS와 BFS

import java.util.*;
import java.io.*;

public class Main {

    static HashSet<Integer> hs;

    static void dfs (ArrayList<Integer> []a, int node) {
        if (!hs.contains(node)) {
            System.out.printf("%d ", node);
            hs.add(node);
            for (int child : a[node]) {
                dfs(a, child);
            }
        }
    }

    public static void main(String[] args) {

        try {
            int n, m, v, tmp1, tmp2;
            ArrayList <Integer> [] arr;
            Deque<Integer> q = new LinkedList<>();
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            hs = new HashSet<>();
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            arr = new ArrayList[n + 1];
            for (int i = 1; i <= n; i++) {
                arr[i] = new ArrayList<Integer>();
            }
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                tmp1 = Integer.parseInt(st.nextToken());
                tmp2 = Integer.parseInt(st.nextToken());
                arr[tmp1].add(tmp2);
                arr[tmp2].add(tmp1);
            }
            for (int i = 1; i <= n; i++) {
                arr[i].sort(Comparator.naturalOrder());
            }
            dfs(arr, v);
            System.out.println();
            hs.clear();
            q.add(v);
            while (!q.isEmpty()) {
                tmp1 = q.poll();
                if (!hs.contains(tmp1)) {
                    System.out.printf("%d ",tmp1);
                    hs.add(tmp1);
                    for (int child : arr[tmp1]) {
                        q.add(child);
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1260
