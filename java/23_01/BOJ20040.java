// 사이클 게임

import java.io.*;
import java.util.*;

public class Main {
    static int [] parentList;
    static boolean compare_parent(int a, int b){
        while(parentList[a] != a){
            a = parentList[a];
        }
        while(parentList[b] != b){
            b = parentList[b];
        }
        if(parentList[a] == parentList[b]){
            return true;
        }
        else{
            return false;
        }
    }

    static void union_parent(int a, int b){
        while(parentList[a] != a){
            a = parentList[a];
        }
        while(parentList[b] != b){
            b = parentList[b];
        }
        if (a > b){
            parentList[a] = b;
        }
        else {
            parentList[b] = a;
        }
    }


    public static void main(String[] args) {
        int nodeNum, n, res = 0, tmpA, tmpB;
        String tmpString;
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st = new StringTokenizer(br.readLine());
            nodeNum = Integer.parseInt(st.nextToken());
            parentList = new int[nodeNum];
            for(int i = 0; i < nodeNum; i++)
            {
                parentList[i] = i;
            }
            n = Integer.parseInt(st.nextToken());
            for(int cnt = 1; cnt <= n; cnt++){
                st = new StringTokenizer(br.readLine());
                tmpA = Integer.parseInt(st.nextToken());
                tmpB = Integer.parseInt(st.nextToken());
                if (compare_parent(tmpA, tmpB)){
                    res = cnt;
                    break;
                }
                union_parent(tmpA, tmpB);
            }
            br.close();
            bw.write(String.valueOf(res));
            bw.flush();
            bw.close();
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/20040
