// 팔

import java.io.*;
import java.util.*;

class Main{

    public static void main(String[] args) {
        try {
            String s1, s2;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            s1 = st.nextToken();
            s2 = st.nextToken();
            int cnt = 0;
            if (s1.length() == s2.length()) {
                for (int i = 0; i < s1.length(); i++) {
                    if (s1.charAt(i) == s2.charAt(i)) {
                        if(s1.charAt(i) == '8'){
                            cnt++;
                        }
                    } else{
                        break;
                    }
                }
            }
            System.out.println(cnt);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

// https://www.acmicpc.net/problem/1105
