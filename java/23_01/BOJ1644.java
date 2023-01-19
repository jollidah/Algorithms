# 소수의 연속합
import java.io.*;
import java.util.*;
 
public class Main {
    static int n;
    static ArrayList<Integer> prime = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        getPrime(n);
        
        int left=0, right=0;
        int ans = 0, sum=2;
        int size = prime.size();
        
        while( left<size && right < size ) {
            if(sum == n) {
                ans++;
                sum -= prime.get(left);
                left++;
            }
            else if(sum >n) {
                sum -= prime.get(left);
                left++;
            }else {
                right++;
                if(right >= size) break;
                sum += prime.get(right);
            }
        }
        
        System.out.println(ans);
        
        sc.close();
    }
    
    // 소수
    static void getPrime(int n) {
        int temp[] = new int[n+1];
        int rootN = (int)Math.sqrt(n);
        for(int i=2; i<=n; i++) {
            temp[i] = i;
        }
        for(int i=2; i<=rootN; i++) {
            if(temp[i] != 0 ) {
                for(int j=i+i; j<=n; j+=i) {
                    temp[j] = 0;
                }
            }
        }
        for(int i=2; i<=n; i++) {
            if(temp[i] != 0) {
                prime.add(temp[i]);
            }
        }    
    }
}
