// 수 찾기

import java.io.*;
import java.util.*;

public class Main {

    public static int binarySearch(int m, int [] arr){
        int lp = 0;
        int rp = arr.length - 1;

        while (lp <= rp){
            int mid = (lp + rp) / 2;
            if (arr[mid] == m){
                return 1;
            }
            else if (m < arr[mid]){
                rp = mid - 1;
            }
            else{
                lp = mid + 1;
            }
        }
        return 0;
    }


    public static void main(String[] args) {
        int n, m;
        int [] inputArray;
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            inputArray = new int [n];
            for (int i = 0; i < n; i++){
            inputArray[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(inputArray);

            m = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++){
                System.out.println(binarySearch(Integer.parseInt(st.nextToken()), inputArray));
            }
            br.close();
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1920
