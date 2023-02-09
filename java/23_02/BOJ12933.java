// 오리

import java.io.*;


public class Main{

    public static void main(String[] args) {
        try{
            int duckNum = 0;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String input = br.readLine();
            String quack = "quack";
            int [] dpTable = new int[quack.length()];
            char tmp;
            for(int i = 0; i < input.length(); i++){
                tmp = input.charAt(i);
                if(tmp == 'q') {
                    dpTable[0]++;
                    if (dpTable[quack.length() - 1] > 0) {
                        dpTable[quack.length() - 1]--;
                    } else {
                        duckNum++;
                    }
                }
                else {
                    for(int j = 1; j < quack.length(); j++){
                        if(tmp == quack.charAt(j)){
                            if(dpTable[j - 1] == 0){
                                duckNum = -1;
                                i = input.length(); // 반복문 종료
                            }
                            dpTable[j - 1]--;
                            dpTable[j]++;
                            break;
                        }
                    }
                }
            }
            for(int i = 0; i < quack.length() - 1;i++){
                if(dpTable[i] != 0){duckNum = -1; break;}
            }
            System.out.println(duckNum);
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/12933
