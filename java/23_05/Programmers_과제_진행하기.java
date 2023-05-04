import java.util.*;

class Solution {
    public String[] solution(String[][] plans) {
        for (String [] tmp : plans){
            tmp[1] = String.valueOf(60 * Integer.parseInt(tmp[1].split(":")[0]) + Integer.parseInt(tmp[1].split(":")[1]));
        }
        ArrayList <String []> data = new ArrayList<> (Arrays.asList(plans));
        Stack <int []> st = new Stack <>();
        data.sort((a, b) -> Integer.parseInt(a[1]) - Integer.parseInt(b[1]));
        int t1, t2, need1, need2, num = 0, p = 0, i = 1;
        String [] answer = new String [plans.length];
        t1 = Integer.parseInt(data.get(0)[1]);
        need1 = Integer.parseInt(data.get(0)[2]);
        while (i < plans.length){
            t2 = Integer.parseInt(data.get(i)[1]);
            need2 = Integer.parseInt(data.get(i)[2]);
            while (t1 + need1 <= t2){
                t1 += need1;
                need1 = 0;
                answer[p++] = data.get(num)[0];
                if (st.isEmpty()){
                    break;                    
                }
                int [] tmp = st.pop();
                num = tmp[0];
                need1 = tmp[1];
            }
            if (t1 + need1 > t2){
                need1 -= t2 - t1;
                st.push(new int [] {num, need1});
            }
            num = i++;
            t1 = t2;
            need1 = need2;
        }
        answer[p++] = data.get(plans.length - 1)[0];
        while (p < plans.length){
            answer[p++] = data.get(st.pop()[0])[0];
        }
        return answer;
    }
}

# https://school.programmers.co.kr/learn/courses/30/lessons/176962#
