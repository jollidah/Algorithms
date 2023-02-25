// N과 M(4)

import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[] nList;


    public static void main(String[] args) {
        try {
            int n, m;
            int [] tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            Queue <int[]> q = new LinkedList<>();
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            for(int i = 1; i <= n; i ++){
                q.add(new int[]{i, m});
            }
            while(!q.isEmpty()){
                tmp = q.poll();
                if(tmp[1] == 1){
                    int div = (int) Math.pow(10, m - 1);
                    while(tmp[0] > 0){
                        System.out.printf("%d ", tmp[0] / div);
                        tmp[0] %= div;
                        div /= 10;
                    }
                    System.out.println();
                } else {
                    for(int i = tmp[0] % 10 ; i <= n; i ++){
                        q.add(new int[]{tmp[0] * 10 + i, tmp[1] - 1});

                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/15652
