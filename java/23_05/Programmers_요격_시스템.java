import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int last = 0;
        int cnt = 0;
        ArrayList <int []> missiles = new ArrayList <>(Arrays.asList(targets));
        missiles.sort((a, b) -> a[1] - b[1]);
        for (int [] missile : missiles){
            if (missile[0] >= last){
                last = missile[1];
                cnt++;
            }
        }
        return cnt;
    }
}

# https://school.programmers.co.kr/learn/courses/30/lessons/181188
