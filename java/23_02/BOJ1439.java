import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        StringTokenizer st1 = new StringTokenizer(s, "0");
        StringTokenizer st0 = new StringTokenizer(s, "1");
        System.out.println(Math.min(st1.countTokens(), st0.countTokens()));
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}


import java.io.*;
//
//
//public class Main{
//    public static void main(String[] args) {
//        try{
//            int res = 0;
//            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//            String s1 = br.readLine();
//            for(int i = 0; i < s1.length() - 1; i++){
//                if (s1.charAt(i) != s1.charAt(i + 1)){
//                    res++;
//                }
//            }
//            bw.write(String.valueOf((res+ 1) / 2));
//            bw.flush();
//        }catch (Exception e){
//            e.printStackTrace();
//        }
//    }
//}

// https://www.acmicpc.net/problem/1439
