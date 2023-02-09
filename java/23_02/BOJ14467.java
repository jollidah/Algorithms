// 소가 길을 건너간 이유 1

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main{
    public static void main(String[] args) {
        try{
            int cowNum, pos, res = 0;
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int n = Integer.parseInt(br.readLine());
            int [] position = new int [11];
            Arrays.fill(position, -1);
            for(int i = 0; i < n; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                cowNum = Integer.parseInt(st.nextToken());
                pos = Integer.parseInt(st.nextToken());
                if(position[cowNum] == -1){
                    position[cowNum] = pos;
                }
                else if(position[cowNum] != pos){
                    res++;
                    position[cowNum] = pos;
                }
            }
            bw.write(String.valueOf(res));
            bw.flush();
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/14467
