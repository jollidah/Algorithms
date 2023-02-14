// Maximum Number of Events That Can Be Attended

import java.util.*;

class Solution {
    public int maxEvents(int[][] events) {
        int cnt = 0, idx = 0, tmp;
        Arrays.sort(events, (a, b) -> a[0] - b[0]);
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int pos = 0;
        while (idx < events.length) {
            pos = events[idx][0];
            while (idx < events.length && events[idx][0] == pos) {
                pq.add(events[idx++][1]);
            }
            while(idx < events.length && !pq.isEmpty() && events[idx][0] > pos) {
                tmp = pq.poll();
                if (tmp >= pos) {
                    pos++;
                    cnt++;
                }
            }
        }
        while(!pq.isEmpty()) {
            tmp = pq.poll();
            if (tmp >= pos) {
                pos++;
                cnt++;
            }
        }
        return cnt;
    }
}

// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/
