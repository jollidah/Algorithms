import java.util.*;

class Solution {
    public long solution(int r1, int r2) {
        double t1 = 1.0 * r1 * r1;
        double t2 = 1.0 * r2 * r2;
        long cnt = 0;
        for (long y = 1; y <= r2; y++){
            double tmp = 1.0 * y * y;
            long x1 = (int) Math.ceil(Math.sqrt(t1 - tmp));
            long x2 = (int) Math.floor(Math.sqrt(t2 - tmp));
            cnt += (x2 - x1 + 1);
        }
        return cnt * 4;
    }
}

# https://school.programmers.co.kr/learn/courses/30/lessons/181187
