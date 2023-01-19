# 그룹 단어 체커

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int n, limit, tmp, ex_tmp, ex_Size, res;
        String tmpString;
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            HashSet<Integer> hs = new HashSet<>();
            n = Integer.parseInt(br.readLine());
            res = n;
            for(int t = 0; t < n; t++){
                tmpString = br.readLine();
                limit = tmpString.length();

                hs.clear();
                ex_tmp = tmpString.charAt(0);
                hs.add(ex_tmp);
                ex_Size = 1;
                for(int i = 1; i < limit; i++){
                    tmp = tmpString.charAt(i);
                    if(tmp != ex_tmp){
                        hs.add(tmp);
                        if(hs.size() == ex_Size){
                            res--;
                            break;
                        }
                        ex_tmp = tmp;
                        ex_Size = hs.size();
                    }
                }
            }
            bw.write(String.valueOf(res));
            bw.flush();
            bw.close();
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}

# https://www.acmicpc.net/problem/1316
