// 고층 건물 1

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int n;
        double tmp, maxH;
        double [] hTable;
        int [] res;
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            hTable = new double[n];
            res = new int[n];
            for(int i = 0; i < n; i++){
                hTable[i] = Double.parseDouble(st.nextToken());
            }
            for(int i = 0; i < n - 1; i++){
                maxH = -Double.MAX_VALUE;
                for(int j = i + 1; j < n; j++){
                    tmp = (hTable[j] - hTable[i]) / (j - i);
                    if (maxH < tmp){
                        res[j]++;
                        res[i]++;
                        maxH = tmp;
                    }
                }
            }
            Arrays.sort(res);
            System.out.println(res[n - 1]);
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1027
