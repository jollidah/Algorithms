# 임시 반장 정하기

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Set<Integer> studentSet;
        int [][] inputTable;
        int n, tmp, maxSize, res;
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st;
            n = Integer.parseInt(br.readLine());
            inputTable = new int[n][5];
            for (int i = 0; i < n; i++)
            {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 5; j++)
                {
                    tmp = Integer.parseInt(st.nextToken());
                    inputTable[i][j] = tmp;
                }
            }
            br.close();
            maxSize = 0;
            res = 0;
            for (int i = 0; i < n; i++)
            {
                studentSet = new HashSet<>();
                for (int j = 0; j < 5; j++)
                {
                    for(int p = 0; p < n; p++){
                        if (inputTable[i][j] == inputTable[p][j]){
                            studentSet.add(p);
                        }
                    }
                }
                if (studentSet.size() > maxSize){
                    res = i;
                    maxSize = studentSet.size();
                }
            }
            bw.write(String.valueOf(res + 1));
            bw.flush();
            bw.close();
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}

# https://www.acmicpc.net/problem/1268
