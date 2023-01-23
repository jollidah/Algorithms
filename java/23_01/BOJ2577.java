// 숫자의 갯수

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        long res = 1, tmpN;
        int [] table = new int[10];
        String tmp;
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            for (int i = 0; i < 3; i++){
                res *= Long.parseLong(br.readLine());
            }
            br.close();
            while (res > 0){
                table[(int) res % 10] += 1;
                res /= 10;
            }
            for(int i = 0; i < 10; i++){
                bw.write(String.valueOf(table[i]) + "\n");
                bw.flush();
            }
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/2577
