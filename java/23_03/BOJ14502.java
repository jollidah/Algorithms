import java.util.*;
import java.io.*;

public class Main {
    static int n, m, cnt, minV = 10000;
    static boolean [][]isVisit;
    static int [][]grid;
    static int [][] tmpGrid;
    static int [][] comb = new int [3][2];
    static int [] dx = new int[] {0, 1, 0, -1};
    static int [] dy = new int[] {1, 0, -1, 0};
    static ArrayList<int[]> virus = new ArrayList<>();


    static void spread(int y, int x){
        for(int i = 0; i < 4; i ++){
            int tmpY = y + dy[i];
            int tmpX = x + dx[i];
            if(tmpY >= 0 && tmpY < n && tmpX >= 0 && tmpX < m && tmpGrid[tmpY][tmpX] == 0){
                cnt++;
                tmpGrid[tmpY][tmpX] = 2;
                spread(tmpY, tmpX);
            }
        }
    }

   static void simulate(){
        isVisit = new boolean [n][m];
        tmpGrid = new int [n][m];
        cnt = 0;
        for(int i = 0; i < n; i ++){
            tmpGrid[i] = grid[i].clone();
       }
        for(int i = 0; i < 3; i ++){
           tmpGrid[comb[i][0]][comb[i][1]] = 1;
       }
        for(int [] v : virus){
           spread(v[0], v[1]);
       }
        minV = Math.min(minV, cnt);
   }

    static void dfs(int y, int x, int cnt){
        if(cnt == 3){
            simulate();
        } else if(y < n){
            dfs(y + (x + 1)/ m, (x + 1) % m , cnt);
            comb[cnt] = new int[]{y, x};
            dfs(y + (x + 1)/ m, (x + 1) % m , cnt + 1);        }
    }


    public static void main(String[] args) {
        try {
            int sum = 0;
            String tmp;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st= new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            grid = new int [n][m];
            for(int i = 0; i < n; i ++){
                st = new StringTokenizer(br.readLine());
                for(int j = 0; j < m; j ++){
                    grid[i][j] =  Integer.parseInt(st.nextToken());
                    if(grid[i][j] == 0){
                        sum++;
                    } else if(grid[i][j] == 2){
                        virus.add(new int [] {i, j});
                    }
                }
            }
            dfs(0, 0, 0);
            System.out.println(sum - minV - 3);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}