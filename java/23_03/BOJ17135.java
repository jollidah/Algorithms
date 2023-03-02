// 캐슬 

import java.util.*;
import java.io.*;

public class Main {

    static int n, m, d;
    static int maxV = 0;
    static ArrayList <int[]> enemyList;
    static int [] comb;
  
  // 궁수의 위치 조합 후, 
    static void simulate(){
        ArrayList <int[]> tmpEnemyList = new ArrayList<>();
        for(int i = 0; i < enemyList.size(); i ++){
               tmpEnemyList.add(enemyList.get(i));
        }
        int cnt = 0;
        int [] tmp = new int [2];
        int[][]target = new int[3][2];
        for(int p = 0;!tmpEnemyList.isEmpty() && p < n; p++){
            for(int j = 0; j < 3; j ++){
                int minD = 100;
                int [] pos = new int[] {-1, -1};
                for(int i = 0; i < tmpEnemyList.size(); i ++){
                    tmp = tmpEnemyList.get(i);
                    if(tmp[0] >= n - p){
                        tmpEnemyList.remove(tmp);
                        continue;
                    }
                    int tmpD = n - tmp[0] + Math.abs(tmp[1] - comb[j]);
                    if(minD == tmpD && tmp[1] < pos[1]){
                        pos = tmp;
                    } else if(minD > tmpD){
                        minD =tmpD;
                        pos = tmp;
                    }
                }
                if(minD <= d + p) {
                    target[j] = pos;
                } else{
                    target[j]= new int[]{-1, -1};
                }
            }
            for(int [] t : target){
                if (tmpEnemyList.remove(t)) {
                    cnt++;
                }

            }
        }
        maxV = Math.max(maxV, cnt);
    }
  
  // 조합 케이스
    static void dfs(int pos, int cnt){
        if (cnt == 3) {
            simulate();
        } else{
            for(int i = pos; i < m + cnt - 2; i ++){
                comb[cnt] = i;
                dfs(i + 1, cnt + 1);
            }
        }
    }
    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st= new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            enemyList = new ArrayList<>();
            comb = new int [3];

            for(int i = 0; i < n; i ++){
                st= new StringTokenizer(br.readLine());
                for(int j = 0; j < m; j ++){
                    if(st.nextToken().equals("1")){
                        enemyList.add(new int [] {i, j});
                    }
                }
            }
            dfs(0, 0);
            System.out.println(maxV);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/17135
