// 럭키 스트레이트

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int n, l, sum = 0;
        String inputData;
        String res;
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            inputData = br.readLine();
            l = inputData.length() / 2;
            n = Integer.parseInt(inputData);
            for (int i = 0 ; i < l; i++){
                sum += n % 10;
                n /= 10;
            }
            for (int i = 0 ; i < l; i++){
                sum -= n % 10;
                n /= 10;
            }
            if (sum == 0){res = "LUCKY";}
            else {res = "READY";}
            br.close();
            bw.write(res);
            bw.flush();
            bw.close();
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
    
    //  https://www.acmicpc.net/problem/18406
}
