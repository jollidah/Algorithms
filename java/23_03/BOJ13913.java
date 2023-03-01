 // 숨바꼭질4
 
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        try {
            int n, m, tmp = 0;
            int [] time = new int[100001];
            int [] parent = new int[100001];
            boolean [] isVisit = new boolean [100001];
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            Queue <Integer> q = new LinkedList<>();
            ArrayList <Integer> al = new ArrayList<>();
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            q.add(n);
            isVisit[n] = true;

            // m이 n보다 작은 경우
            if (m < n){
                System.out.println(n - m);
                while(n >= m){
                    System.out.printf("%d ", n--);
                }
                System.exit(0);
            }
            
         // BFS
            while(!q.isEmpty()){
                tmp = q.poll();
                if(tmp == m){
                    System.out.println(time[tmp]);
                    break;
                } else{
                    if(tmp < m && tmp * 2 <= 100000 && !isVisit[tmp * 2]){
                        isVisit[tmp * 2] = true;
                        time[tmp * 2] = time[tmp] + 1;
                        parent[tmp * 2] = tmp;
                        q.add(tmp * 2);
                    }
                    if(tmp < m && tmp + 1 <= 100000 && !isVisit[tmp + 1]){
                        isVisit[tmp + 1] = true;
                        time[tmp + 1] = time[tmp] + 1;
                        parent[tmp + 1] = tmp;
                        q.add(tmp + 1);
                    }
                    if(tmp - 1 >= 0 && !isVisit[tmp - 1]){
                        isVisit[tmp - 1] = true;
                        time[tmp - 1] = time[tmp] + 1;
                        parent[tmp - 1] = tmp;
                        q.add(tmp - 1);
                    }
                }
            }
            // 출처 추적
            while(tmp != n){
                al.add(tmp);
                tmp = parent[tmp];
            }
            System.out.printf("%d ", n);
            for(int i = al.size() - 1; i >= 0; i --){
                System.out.printf("%d ", al.get(i));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

 
 // https://www.acmicpc.net/problem/13913
