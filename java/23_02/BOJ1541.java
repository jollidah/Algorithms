// 잃어버린 괄호

import java.util.*;
import java.io.*;

public class Main {


    public static void main(String[] args) {
        try {
            int res, tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine(), "+-", true);
            res = Integer.parseInt(st.nextToken());
            while (st.hasMoreTokens()) {
                if (st.nextToken().equals("+")) {
                    res += Integer.parseInt(st.nextToken());
                } else {
                    tmp = Integer.parseInt(st.nextToken());
                    while (st.hasMoreTokens()) {
                        st.nextToken();
                        tmp += Integer.parseInt(st.nextToken());
                    }
                    res -= tmp;
                }
            }
            System.out.println(res);
        } catch (Exception e) {
        }
    }
}

// https://www.acmicpc.net/problem/1541
