// 단어 뒤집기 2

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int n, k, idx = 0;
        String tmp;
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st = new StringTokenizer(br.readLine(), " <>", true);
            while (st.hasMoreTokens()){
                tmp = st.nextToken();
                if (tmp.equals("<")){
                    bw.write(tmp);
                    while(!(tmp = st.nextToken()).equals(">")){
                        bw.write(tmp);
                    }
                    bw.write(tmp);
                }
                else {
                    n = tmp.length() - 1;
                    for(int i = n; i >= 0; i--){
                        bw.write(tmp.charAt(i));
                    }
                }
            }
            bw.flush();
            bw.close();
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/17413
