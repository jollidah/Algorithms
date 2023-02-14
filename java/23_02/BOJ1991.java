// 

import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {

    public static int[][] tree;
    public static void preOrder(int pos){
        System.out.print((char) (pos + 'A'));
        if(tree[pos][0] != -1){
            preOrder(tree[pos][0]);
        }
        if (tree[pos][1] != -1) {
            preOrder(tree[pos][1]);
        }
    }

    public static void inOrder(int pos){
        if(tree[pos][0] != -1){
            inOrder(tree[pos][0]);
        }
        System.out.print((char) (pos + 'A'));
        if (tree[pos][1] != -1) {
            inOrder(tree[pos][1]);
        }
    }

    public static void postOrder(int pos){
        if(tree[pos][0] != -1){
            postOrder(tree[pos][0]);
        }
        if (tree[pos][1] != -1) {
            postOrder(tree[pos][1]);
        }
        System.out.print((char) (pos + 'A'));
    }

    public static void main(String[] args) {
        try{
            int n, idx;
            String inputString;
            char tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            n = Integer.parseInt(br.readLine());
            tree = new int[n][2];
            for (int i = 0; i < n; i++) {
                inputString = br.readLine();
                idx = (inputString.charAt(0) - 'A');
                for (int j = 1; j < 3; j++) {
                    tmp = inputString.charAt(2 * j);
                    if(tmp == '.'){
                        tree[idx][j - 1] = -1;
                    }
                    else{
                        tree[idx][j - 1] = tmp - 'A';
                    }
                }
            }
            preOrder(0);
            System.out.println();
            inOrder(0);
            System.out.println();
            postOrder(0);
            System.out.println();


        }catch (Exception e){
            e.printStackTrace();
        }
    }
}

// https://www.acmicpc.net/problem/1991
