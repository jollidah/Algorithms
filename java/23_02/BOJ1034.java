// 램프

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        try {
            int n, m, k, s, cnt, maxV;
            int [] tmpList = new int [2];
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            HashMap <String, int[]> hm = new HashMap<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            String tmp;
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            // 0 갯수 확인 후, HashMap에 0 갯수와 같은 라인 갯수
            for(int i = 0; i < n; i++){
                tmp = br.readLine();
                cnt = 0;
                for(int j = 0; j < m; j++){
                    if(tmp.charAt(j) == '0'){
                        cnt++;
                    }
                }
                if(hm.containsKey(tmp)){
                    tmpList = hm.get(tmp);
                    hm.replace(tmp, new int[] {tmpList[0] + 1, tmpList[1]});
                } else{
                    hm.put(tmp, new int[]{1, cnt});
                }
            }
            k = Integer.parseInt(br.readLine());

            // 2로 나눈 나머지값 확인
            s = k % 2;
            maxV = 0;
            for(String key : hm.keySet()){
                tmpList = hm.get(key);
                if(tmpList[1] <= k && tmpList[1] % 2 == s){
                    maxV = Math.max(maxV, tmpList[0]);
                }
            }
            System.out.println(maxV);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1034
