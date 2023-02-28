// 노드사이의 거리

import java.util.*;
import java.io.*;

public class Main {
    static boolean isVisit [];
    static ArrayList <int[]> [] arr;

    static int dfs(int s, int e, int dist){
        if(s == e){
            return dist;
        } else{
            isVisit[s] = true;
            for(int[] seq : arr[s]){
                if(!isVisit[seq[0]]){
                    int tmpRes = dfs(seq[0], e, dist + seq[1]);
                    if(tmpRes != 0){
                        return tmpRes;
                    }
                }
            }
            return 0;
        }
    }


    public static void main(String[] args) {
        try {
            int n, m, a, b, c, cnt;
            int [] tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            arr = new ArrayList [n + 1];
            for(int i = 1; i <= n; i ++){
                arr[i] = new ArrayList<>();
            }
            for(int i = 0; i < n - 1; i++){
                st = new StringTokenizer(br.readLine());
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());
                c = Integer.parseInt(st.nextToken());
                arr[a].add(new int[] {b, c});
                arr[b].add(new int[] {a, c});
            }
            while(m-- > 0){
                isVisit = new boolean [n + 1];
                st = new StringTokenizer(br.readLine());
                bw.write(String.valueOf(dfs(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), 0)));
                bw.write("\n");
            }
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1240
