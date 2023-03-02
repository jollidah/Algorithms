// 

import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static int maxV = 0;
    static int [] arr;
    static int [] table;
    static boolean isVisit[];

    // 합이 50인 수열을 찾는 투포인터 함수
    static void calc() {
        int lp = 0;
        int rp = 1;
        int sum = arr[0];
        int cnt = 0;
        while (rp < n) {
            if (sum == 50) {
                cnt++;
                sum += arr[rp++];
                sum -= arr[lp++];
            } else if (sum > 50) {
                sum -= arr[lp++];
            } else {
                sum += arr[rp++];
            }
        }
        while (sum > 50 && lp < rp) {
            if (sum == 50) {
                cnt++;
            }
            sum -= arr[lp++];
        }
        maxV = Math.max(maxV, cnt);
    }

    // 수열 (중복 허용)
    static void dfs(int idx){

        if(idx == n){
            calc();
        } else{
            for(int i = 0 ; i < n; i ++){
                if(!isVisit[i]){
                    isVisit[i] = true;
                    arr[idx] = table[i];
                    dfs(idx + 1);
                    isVisit[i] = false;
                }
            }
        }
    }

    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            n = Integer.parseInt(br.readLine());
            arr = new int [n];
            table = new int [n];
            isVisit = new boolean [n];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i = 0; i < n; i++){
                table[i] = Integer.parseInt(st.nextToken());
                // 요소가 50이 넘어가는 순간 프로그램 종료
                if(table[i] > 50){
                    System.out.println(0);
                    System.exit(0);
                }
            }
            dfs(0);
            System.out.println(maxV);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}


// https://www.acmicpc.net/problem/1239
