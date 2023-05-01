import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        String [] answer = new String[players.length];
        HashMap <String, Integer> hm = new HashMap <>();
        int n = players.length;
        for (int i = 0; i < n; i ++){
            hm.put(players[i], i);
            answer[i] = players[i];
        }
        String tmp;
        for (String call : callings){
            int i = hm.get(call);
            tmp = answer[i - 1];
            answer[i] = tmp;
            answer[i - 1] = call;
            hm.replace(tmp, i);
            hm.replace(call, i - 1);
        }
        return answer;
    }
}

# https://school.programmers.co.kr/learn/courses/30/lessons/178871
